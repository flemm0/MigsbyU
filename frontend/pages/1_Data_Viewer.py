import requests
import polars as pl
import streamlit as st



st.set_page_config(
    layout='wide'
)

def add_student(data):
    response = requests.post(
        'http://api:8000/students/',
        json=data,
        headers={'accept': 'application/json'}
    )
    return response.status_code


def display_student_table():
    response = requests.get(
        'http://api:8000/students/?skip=0&limit=100', 
        headers={'accept': 'application/json'}
    )
    st.header('Table: *Students* :male-student: :female-student:', divider='gray')
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


with st.container():
    display_student_table()


with st.expander('Add New Student'):
    with st.form('Student Add Form'):
        st.write('Register new student at MigsbyU')
        id = st.text_input(label='id')
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
            status_code = add_student(new_student_data)
            if status_code == 200:
                st.success('New student added successfully!')
            else:
                st.error(f'Failed to add new student. Status code: {status_code}')
            st.rerun()
