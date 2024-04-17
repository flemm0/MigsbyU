def dimension_table_query(table: str, columns: list[str]) -> str:
    columns_str = ', '.join(columns)

    query = f"""
    CREATE OR REPLACE TEMPORARY SEQUENCE surrogate_key_gen;
    CREATE OR REPLACE TABLE {table}_dimension AS (
        WITH base_table AS (
            SELECT
                nextval('surrogate_key_gen') AS {table[:-1]}_key,
                * 
            FROM '/data_lake/{table}/data/*.parquet'
        ),
        current_row_indicator_added AS (
            SELECT *,
                CASE WHEN source_datetime = max_source_datetime THEN 'yes' ELSE 'no' END AS current_row_indicator
            FROM  (
                SELECT *,
                    MAX(source_datetime) OVER (PARTITION BY id) AS max_source_datetime
                FROM base_table
            ) temp
        ),
        end_effective_date_added AS (
        SELECT *,
            CASE
                WHEN current_row_indicator = 'yes' then '9999-12-30'
                ELSE LEAD(source_datetime) OVER (PARTITION BY id ORDER BY source_datetime)
            END AS effective_date_end
        FROM current_row_indicator_added
        ),
        final AS (
            SELECT
                {table[:-1]}_key,
                {columns_str},
                source_datetime::timestamp AS effective_date_start,
                effective_date_end::timestamp - interval 1 second AS effective_date_end,
                current_row_indicator
            FROM end_effective_date_added
            ORDER BY {table[:-1]}_key
        )
        SELECT *
        FROM final
    );
    """

    return query


## TODO eliminate need for semicolon ; in creating temp sequence in the middle of query
def fact_table_query() -> str:
    query = f"""
    {dimension_table_query(table='students', columns=['id', 'first_name', 'last_name', 'gender', 'address', 'major', 'year_of_study', 'gpa', 'enrollment_status'])}
    {dimension_table_query(table='professors', columns=['id', 'title', 'first_name', 'last_name', 'gender', 'address', 'department', 'date_of_birth', 'annual_salary'])}
    {dimension_table_query(table='courses', columns=['id', 'name', 'units', 'department'])}
    CREATE OR REPLACE TABLE course_enrollment_fact AS (
    WITH student_enrollments AS (
        SELECT 
            student_key,
            course_key,
            takes.*
        FROM '/data_lake/takes/data/*.parquet' AS takes
        JOIN students_dimension
        ON students_dimension.id = takes.student_id
        JOIN courses_dimension 
        ON courses_dimension.id = takes.course_id
        WHERE source_datetime::timestamp BETWEEN students_dimension.effective_date_start AND students_dimension.effective_date_end
        AND source_datetime::timestamp BETWEEN courses_dimension.effective_date_start AND courses_dimension.effective_date_end
    ),
    professor_assignments AS (
        SELECT
            professor_key,
            course_key,
            teaches.*
        FROM '/data_lake/teaches/data/*.parquet' AS teaches
        JOIN professors_dimension
        ON professors_dimension.id = teaches.professor_id
        JOIN courses_dimension
        ON courses_dimension.id = teaches.course_id
        WHERE source_datetime::timestamp BETWEEN professors_dimension.effective_date_start AND professors_dimension.effective_date_end
        AND source_datetime::timestamp BETWEEN courses_dimension.effective_date_start AND courses_dimension.effective_date_end
    ),
    final AS (
        SELECT
            student_key,
            professor_key,
            COALESCE(student_enrollments.course_key, professor_assignments.course_key) AS course_key,
            COALESCE(student_enrollments.semester, professor_assignments.semester) AS semester,
            course_enrollment_count
        FROM student_enrollments
        FULL JOIN professor_assignments
        ON student_enrollments.course_id = professor_assignments.course_id
    )
    SELECT *
    FROM final
    );
    """
    return query