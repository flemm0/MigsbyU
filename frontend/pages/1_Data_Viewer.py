import requests
import polars as pl
import streamlit as st

from datetime import datetime

import json

from utils import *


st.set_page_config(
    layout='wide'
)


student_tab, professor_tab, course_tab, takes_tab, teaches_tab = st.tabs(['Students', 'Professors', 'Courses', 'Enrollments', 'Assignments'])


with student_tab:

    with st.container():
        response = requests.get(
            'http://api:8000/students/?skip=0&limit=100', 
            headers={'accept': 'application/json'}
        )
        st.header('Table: **Students** :male-student: :female-student:', divider='gray')
        if response.status_code == 200:
            data = response.json()
            table = pl.DataFrame(data).to_pandas()
            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f'Error getting API response: {response.status_code}')

    with st.expander('Generate Random Students'):
        n_students = st.number_input(
            label='Choose number of students to generate',
            min_value=1
        )
        if st.button('Submit', type='primary', key='generate_random_student'):
            new_students = generate_random_students(n=n_students)
            for student in new_students:
                requests.post('http://api:8000/students/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(student, default=str))
            st.rerun()

    with st.expander('Add New Student'):
        with st.form('Student Add Form'):
            st.write('Register new student at MigsbyU')
            id = st.text_input(label='ID')
            first_name = st.text_input(label='First Name')
            last_name = st.text_input(label='Last Name')
            gender = st.text_input(label='Gender')
            address = st.text_input(label='Address')
            date_of_birth = st.date_input(label='Date of Birth')
            major = st.text_input(label='Major')
            year_of_study = st.number_input(label='Year of Study', min_value=1)
            gpa = st.number_input(label='GPA', min_value=0.0, max_value=4.0)
            enrollment_status = st.selectbox(
                label='Enrollment Status',
                options=['Full-time', 'Part-time']
            )
            submit = st.form_submit_button('Submit')

            if submit:
                new_student_data = {
                    'id': id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'address': address,
                    'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
                    'major': major,
                    'year_of_study': year_of_study,
                    'gpa': gpa,
                    'enrollment_status': enrollment_status
                }
                status_code = add_record(data=new_student_data, table='students')
                if status_code == 200:
                    st.success('New student added successfully!')
                else:
                    st.error(f'Failed to add new student. Status code: {status_code}')
                st.rerun()

    with st.expander('Edit Student Data'):
            st.write('Edit currently enrolled student\'s data')
            student_id = st.text_input(label='Student ID to edit', max_chars=10)
            if student_id:
                    response = requests.get(f'http://api:8000/students/{student_id}', headers={'accept': 'application/json'})
                    if response.status_code != 200:
                        st.write('Student ID not found!')
                    else:
                        with st.form('Student Edit Form'):
                            student = response.json()
                            first_name = st.text_input(label='First Name', value=student.get('first_name'))
                            last_name = st.text_input(label='Last Name', value=student.get('last_name'))
                            gender = st.text_input(label='Gender', value=student.get('gender'))
                            address = st.text_input(label='Address', value=student.get('address'))
                            date_of_birth = st.date_input(label='Date of Birth', value=datetime.strptime(student.get('date_of_birth'), '%Y-%m-%d'))
                            major = st.text_input(label='Major', value=student.get('major'))
                            year_of_study = st.number_input(label='Year of Study', min_value=1, value=student.get('year_of_study'))
                            gpa = st.number_input(label='GPA', min_value=0.0, max_value=4.0, value=student.get('gpa'))
                            enrollment_status = st.selectbox(
                                label='Enrollment Status',
                                options=['Full-time', 'Part-time']
                            )
                    
                            submit = st.form_submit_button('Submit')

                            if submit:
                                new_student_data = {
                                    'id': student_id,
                                    'first_name': first_name,
                                    'last_name': last_name,
                                    'gender': gender,
                                    'address': address,
                                    'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
                                    'major': major,
                                    'year_of_study': year_of_study,
                                    'gpa': gpa,
                                    'enrollment_status': enrollment_status
                                }

                                status_code = edit_record(data=new_student_data, id=student_id, table='students')
                                if status_code == 200:
                                    st.success('Student updated successfully!')
                                else:
                                    st.error(f'Failed to update student. Status code: {status_code}')
                                st.rerun()


with professor_tab:

    with st.container():
        response = requests.get(
            'http://api:8000/professors/', 
            headers={'accept': 'application/json'}
        )
        st.header('Table: **Professors** :male-teacher: :female-teacher:', divider='gray')
        if response.status_code == 200:
            data = response.json()
            table = pl.DataFrame(data).to_pandas()
            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f'Error getting API response: {response.status_code}')

    with st.expander('Generate Random Professors'):
        n_professors = st.number_input(
            label='Choose number of professors to generate',
            min_value=1
        )
        if st.button('Submit', type='primary', key='generate_random_professor'):
            new_professors = generate_random_professors(n=n_professors)
            for professor in new_professors:
                requests.post('http://api:8000/professors/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(professor, default=str))
            st.rerun()

    with st.expander('Add New Professor'):
        with st.form('Professor Add Form'):
            st.write('Register new professor at MigsbyU')
            id = st.text_input(label='ID')
            title = st.text_input(label='Title', value='Dr.')
            first_name = st.text_input(label='First Name')
            last_name = st.text_input(label='Last Name')
            gender = st.text_input(label='Gender')
            address = st.text_input(label='Address')
            date_of_birth = st.date_input(label='Date of Birth')
            annual_salary = st.number_input(label='Annual Salary', step=5000)
            submit = st.form_submit_button('Submit')

            if submit:
                new_professor_data = {
                    'id': id,
                    'title': title,
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'address': address,
                    'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
                    'annual_salary': annual_salary
                }
                status_code = add_record(data=new_professor_data, table='professors')
                if status_code == 200:
                    st.success('New student added successfully!')
                else:
                    st.error(f'Failed to add new student. Status code: {status_code}')
                st.rerun()

    with st.expander('Edit Professor Data'):
            st.write('Edit currently employed professor\'s data')
            professor_id = st.text_input(label='Professor ID to edit', max_chars=10)
            if professor_id:
                    response = requests.get(f'http://api:8000/professors/{professor_id}', headers={'accept': 'application/json'})
                    if response.status_code != 200:
                        st.write('Professor ID not found!')
                    else:
                        with st.form('Professor Edit Form'):
                            professor = response.json()
                            first_name = st.text_input(label='First Name', value=professor.get('first_name'))
                            title = st.text_input(label='Title', value=professor.get('title'))
                            last_name = st.text_input(label='Last Name', value=professor.get('last_name'))
                            gender = st.text_input(label='Gender', value=professor.get('gender'))
                            address = st.text_input(label='Address', value=professor.get('address'))
                            date_of_birth = st.date_input(label='Date of Birth', value=datetime.strptime(professor.get('date_of_birth'), '%Y-%m-%d'))
                            department = st.text_input(label='Department', value=professor.get('department'))
                            annual_salary = st.number_input(label='Annual Salary', step=5000, value=professor.get('annual_salary'))
                    
                            submit = st.form_submit_button('Submit')

                            if submit:
                                new_professor_data = {
                                    'id': professor_id,
                                    'title': title,
                                    'first_name': first_name,
                                    'last_name': last_name,
                                    'gender': gender,
                                    'address': address,
                                    'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
                                    'department': department,
                                    'annual_salary': annual_salary
                                }

                                status_code = edit_record(data=new_professor_data, id=professor_id, table='professors')
                                if status_code == 200:
                                    st.success('Professor updated successfully!')
                                else:
                                    st.error(f'Failed to update professor. Status code: {status_code}')
                                st.rerun()


with course_tab:

    with st.container():
        response = requests.get(
            'http://api:8000/courses/', 
            headers={'accept': 'application/json'}
        )
        st.header('Table: **Courses** :school:', divider='gray')
        if response.status_code == 200:
            data = response.json()
            table = pl.DataFrame(data).to_pandas()
            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f'Error getting API response: {response.status_code}')

    with st.expander('Generate Random Courses'):
        n_courses = st.number_input(
            label='Choose number of courses to generate',
            min_value=1
        )
        if st.button('Submit', type='primary', key='generate_random_course'):
            new_courses = generate_random_courses(n=n_courses)
            for course in new_courses:
                requests.post('http://api:8000/courses/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(course, default=str))
            st.rerun()

    with st.expander('Add New Course'):
        with st.form('Course Add Form'):
            st.write('Register new course at MigsbyU')
            id = st.text_input(label='ID')
            name = st.text_input(label='Name')
            units = st.number_input(label='Units', min_value=1, max_value=4)
            department = st.text_input(label='Department')
            submit = st.form_submit_button('Submit')

            if submit:
                new_course_data = {
                    'id': id,
                    'name': name,
                    'units': units,
                    'department': department
                }
                status_code = add_record(data=new_course_data, table='courses')
                if status_code == 200:
                    st.success('New course added successfully!')
                else:
                    st.error(f'Failed to add new course. Status code: {status_code}')
                st.rerun()

    with st.expander('Edit Course Data'):
            st.write('Edit currently course\'s data')
            course_id = st.text_input(label='Course ID to edit', max_chars=10)
            if course_id:
                    response = requests.get(f'http://api:8000/professors/{course_id}', headers={'accept': 'application/json'})
                    if response.status_code != 200:
                        st.write('Course ID not found!')
                    else:
                        with st.form('Course Edit Form'):
                            course = response.json()
                            name = st.text_input(label='Course Name', value=course.get('name'))
                            units = st.number_input(label='Units', min_value=1, max_value=4, value=course.get('units'))
                            department = st.text_input(label='Department', value=course.get('department'))
                    
                            submit = st.form_submit_button('Submit')

                            if submit:
                                new_course_data = {
                                    'id': course_id,
                                    'name': name,
                                    'units': units,
                                    'department': department
                                }

                                status_code = edit_record(data=new_course_data, id=course_id, table='courses')
                                if status_code == 200:
                                    st.success('Course updated successfully!')
                                else:
                                    st.error(f'Failed to update course. Status code: {status_code}')
                                st.rerun()


with takes_tab:

    with st.container():
        response = requests.get(
            'http://api:8000/enrollments/', 
            headers={'accept': 'application/json'}
        )
        st.header('Table: **Takes** :book:', divider='gray')
        if response.status_code == 200:
            data = response.json()
            table = pl.DataFrame(data).to_pandas()
            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f'Error getting API response: {response.status_code}')

    with st.expander('Register Student In Course'):
        with st.form('Student Enrollment Form'):
            student_id = st.text_input('Student ID')
            course_id = st.text_input('Course ID')
            sem = st.selectbox(label='Semester', options=['Fall', 'Spring'])
            year = st.number_input(label='Year', min_value=1990, max_value=datetime.today().year, value=datetime.today().year)
            submit = st.form_submit_button('Submit')

            if submit:
                new_enrollment = {
                    'student_id': student_id,
                    'course_id': course_id,
                    'semester': sem + ' ' + str(year)
                }
                status_code = add_record(data=new_enrollment, table='enrollments')
                if status_code == 200:
                    st.success('New enrollment added successfully!')
                else:
                    st.error(f'Failed to add new enrollment. Status code: {status_code}')
                st.rerun()

    with st.expander('Drop Student From Course'):
        with st.form('Student Drop Enrollment Form'):
            student_id = st.text_input('Student ID')
            course_id = st.text_input('Course ID')
            sem = st.selectbox(label='Semester', options=['Fall', 'Spring'])
            year = st.number_input(label='Year', min_value=1990, max_value=datetime.today().year, value=datetime.today().year)
            submit = st.form_submit_button('Submit')

            if submit:
                existing_enrollment = {
                    'student_id': student_id,
                    'course_id': course_id,
                    'semester': sem + ' ' + str(year)
                }
                status_code = drop_record(data=existing_enrollment, table='enrollments')
                if status_code == 200:
                    st.success('Enrollment dropped successfully!')
                    st.rerun()
                else:
                    st.error(f'Failed to drop enrollment. {status_code}')


with teaches_tab:

    with st.container():
        response = requests.get(
            'http://api:8000/assignments/',
            headers={'accept': 'application/json'}
        )
        st.header('Table: **Teaches** :pencil:', divider='gray')
        if response.status_code == 200:
            data = response.json()
            table = pl.DataFrame(data).to_pandas()
            st.dataframe(
                table,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f'Error getting API response: {response.status_code}')

    with st.expander('Assign Professor To Teach Course'):
        with st.form('Professor Assignment Form'):
            professor_id = st.text_input('Professor ID')
            course_id = st.text_input('Course ID')
            sem = st.selectbox(label='Semester', options=['Fall', 'Spring'])
            year = st.number_input(label='Year', min_value=1990, max_value=datetime.today().year, value=datetime.today().year)
            submit = st.form_submit_button('Submit')

            if submit:
                new_assignment = {
                    'professor_id': professor_id,
                    'course_id': course_id,
                    'semester': sem + ' ' + str(year)
                }
                status_code = add_record(data=new_assignment, table='assignments')
                if status_code == 200:
                    st.success('New assignment added successfully!')
                else:
                    st.error(f'Failed to add new assignment. Status code: {status_code}')
                st.rerun()

    with st.expander('Drop Professor From Course'):
        with st.form('Professor Drop Enrollment Form'):
            professor_id = st.text_input('Professor ID')
            course_id = st.text_input('Course ID')
            sem = st.selectbox(label='Semester', options=['Fall', 'Spring'])
            year = st.number_input(label='Year', min_value=1990, max_value=datetime.today().year, value=datetime.today().year)
            submit = st.form_submit_button('Submit')

            if submit:
                existing_assignment = {
                    'professor_id': professor_id,
                    'course_id': course_id,
                    'semester': sem + ' ' + str(year)
                }
                status_code = drop_record(data=existing_assignment, table='assignments')
                if status_code == 200:
                    st.success('Assignment dropped successfully!')
                    st.rerun()
                else:
                    st.error(f'Failed to drop assignment. {status_code}')