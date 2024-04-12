import duckdb
import streamlit as st



st.set_page_config(
    layout='wide'
)



student_tab, professor_tab, course_tab, takes_tab, teaches_tab = st.tabs(['Students Dimension', 'Professors Dimension', 'Courses Dimension', 'Enrollments Fact', 'Assignments Fact'])

with student_tab:

    with st.container():
        st.header('Table: **Students Dimension** :male-student: :female-student:', divider='gray')
        query = f"""
        WITH current_row_indicator_added AS (
            SELECT *,
                CASE WHEN source_datetime = max_source_datetime THEN 'yes' ELSE 'no' END AS current_row_indicator
            FROM  (
                SELECT *,
                    MAX(source_datetime) OVER (PARTITION BY id) AS max_source_datetime
                FROM '/data_lake/students/data/*.parquet'
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
                id,
                first_name,
                last_name,
                gender,
                address,
                date_of_birth,
                major,
                year_of_study,
                gpa,
                enrollment_status,
                source_datetime::timestamp AS effective_date_start,
                effective_date_end::timestamp - interval 1 second AS effective_date_end,
                current_row_indicator
            FROM end_effective_date_added
            ORDER BY id
        )
        SELECT *
        FROM final
        """
        table = duckdb.sql(query=query).df()
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

        refresh_button = st.button(label='Refresh Data')
        if refresh_button:
            st.rerun()