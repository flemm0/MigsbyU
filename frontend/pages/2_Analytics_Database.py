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
        SELECT * FROM '/data_lake/students/data/*.parquet'; 
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