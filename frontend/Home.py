import streamlit as st
import requests


st.write('Hello World!')

selected_student_id = st.text_input(label='Select student id')
if selected_student_id:
    response = requests.get(f'http://localhost:8000/students/{selected_student_id}', headers={'accept': 'application/json'})
    if response.status_code == 200:
        st.write(response.json())