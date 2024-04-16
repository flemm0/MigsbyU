import duckdb
import streamlit as st

from sql import dimension_table_query, fact_table_query



st.set_page_config(
    layout='wide'
)



students_tab, professors_tab, courses_tab, enrollments_tab = st.tabs(['Students Dimension', 'Professors Dimension', 'Courses Dimension', 'Course Enrollments Fact'])

with students_tab:

    with st.container():
        st.header('Table: **Students Dimension** :male-student: :female-student:', divider='gray')
        query = dimension_table_query(table='students', columns=['id', 'first_name', 'last_name', 'gender', 'address', 'major', 'year_of_study', 'gpa', 'enrollment_status'])
        duckdb.sql(query=query)
        table = duckdb.sql('SELECT * FROM students_dimension').df()
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

        refresh_button = st.button(label='Refresh Student Data')
        if refresh_button:
            st.rerun()


with professors_tab:

    with st.container():
        st.header('Table: **Professors Dimension** :male-teacher: :female-teacher:', divider='gray')
        query = dimension_table_query(table='professors', columns=['id', 'title', 'first_name', 'last_name', 'gender', 'address', 'department', 'date_of_birth', 'annual_salary'])
        duckdb.sql(query=query)
        table = duckdb.sql('SELECT * FROM professors_dimension').df()
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

        refresh_button = st.button(label='Refresh Professor Data')
        if refresh_button:
            st.rerun()


with courses_tab:

    with st.container():
        st.header('Table: **Courses Dimension** :school:', divider='gray')
        query = dimension_table_query(table='courses', columns=['id', 'name', 'units', 'department'])
        duckdb.sql(query=query)
        table = duckdb.sql('SELECT * FROM courses_dimension').df()
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

        refresh_button = st.button(label='Refresh Course Data')
        if refresh_button:
            st.rerun()


with enrollments_tab:

    with st.container():
        st.header('Table: **Course Enrollments Fact** :school:', divider='gray')
        query = fact_table_query()
        duckdb.sql(query=query)
        table = duckdb.sql('SELECT * FROM course_enrollment_fact').df()
        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )

        refresh_button = st.button(label='Refresh Course Enrollment/Assignment Data')
        if refresh_button:
            st.rerun()