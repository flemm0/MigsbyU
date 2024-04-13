def dimension_table_query(table: str, columns: list[str]) -> str:
    columns_str = ', '.join(columns)

    query = f"""
    WITH current_row_indicator_added AS (
        SELECT *,
            CASE WHEN source_datetime = max_source_datetime THEN 'yes' ELSE 'no' END AS current_row_indicator
        FROM  (
            SELECT *,
                MAX(source_datetime) OVER (PARTITION BY id) AS max_source_datetime
            FROM '/data_lake/{table}/data/*.parquet'
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
            {columns_str},
            source_datetime::timestamp AS effective_date_start,
            effective_date_end::timestamp - interval 1 second AS effective_date_end,
            current_row_indicator
        FROM end_effective_date_added
        ORDER BY id
    )
    SELECT *
    FROM final
    """

    return query