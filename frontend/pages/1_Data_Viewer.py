import requests
import polars as pl
import streamlit as st



students_tab, professors_tab = st.tabs(['Students', 'Professors'])

with students_tab:
    response = requests.get(
        'http://api:8000/students/?skip=0&limit=100', 
        headers={'accept': 'application/json'}
    )
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

    with st.form('Student Add Form'):
        st.write('Register new student at MigsbyU')
        id = st.text_input(label='id')
        first_name = st.text_input(label='First Name')
        last_name = st.text_input(label='Last Name')
        gender = st.text_input(label='Gender')
        address = st.text_input(label='Address')
        date_of_birth = st.date_input(label='Date of Birth')
        major = st.text_input(label='major')
        year_of_study = st.number_input(label='Year of Study', min_value=1)
        gpa = st.number_input(label='GPA', min_value=0.0, max_value=4.0)
        enrollment_status = st.multiselect(
            label='Enrollment Status',
            options=['Full-time', 'Part-time']
        )
        submit = st.form_submit_button('Submit')

        if submit:
            data = {
                'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'gender': gender,
                'address': address,
                'date_of_birth': date_of_birth,
                'major': major,
                'year_of_study': year_of_study,
                'gpa': gpa,
                'enrollment_status': enrollment_status
            }
            st.write(data)