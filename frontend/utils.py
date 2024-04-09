from faker import Faker
import random
import requests
import uuid

import config


def add_record(data: dict, table: str):
    response = requests.post(
        f'http://api:8000/{table}/',
        json=data,
        headers={'accept': 'application/json'}
    )
    return response.status_code


def edit_record(data: dict, id: str, table: str):
    response = requests.put(
        f'http://api:8000/{table}/{id}',
        json=data,
        headers={'accept': 'application/json'}
    )



def generate_random_id(table: str) -> str:
    response = requests.get(f'http://api:8000/{table}/', headers={'accept': 'application/json'})
    data = response.json()
    existing_ids = [record['id'] for record in data]
    id = uuid.uuid4().hex[:10].upper()
    while id in existing_ids:
        generate_random_id()
    return id
    

def generate_random_students(n: int) -> list[dict]:
    fake = Faker()
    students = []
    for i in range(0, n):
        id = generate_random_id(table='students')
        male = random.choice([True, False])
        if male:
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            gender = 'Male'
        else:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            gender = 'Female'
        address = fake.address()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=26)
        major = fake.random_element(
            elements=(
                'Computer Science', 
                'Data Science',
                'Engineering', 
                'Psychology', 
                'Biology', 
                'Chemistry',
                'Business', 
                'Art History', 
                'English Literature', 
                'Mathematics', 
                'Economics', 
                'Sociology', 
                'Political Science', 
                'Physics',
                'Undeclared'
            )
        )
        year_of_study = random.choices([1, 2, 3, 4, 5, 6], weights=[20, 20, 20, 20, 2, 1])[0]
        gpa_range = random.choices([(0, 2), (2, 3), (3, 3.5), (3.5, 4)], weights=[2, 4, 6, 8])[0]
        gpa = round(random.uniform(gpa_range[0], gpa_range[1]), 2)
        enrollment_status = random.choices(['Full-time', 'Part-time'], weights=[40, 1])[0]
        students.append(
            {
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
        )
    return students


def generate_random_professors(n: int) -> list[dict]:
    fake = Faker()
    professors = []
    for i in range(0, n):
        id = generate_random_id(table='professors')
        male = random.choice([True, False])
        if male:
            title = random.choices(['Dr.', 'Mr.'], weights=[10, 1])[0]
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            gender = 'Male'
        else:
            title = random.choices(['Dr.', 'Mrs.', 'Ms.'], weights=[10, .5, .5])[0]
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            gender = 'Female'
        address = fake.address()
        date_of_birth = fake.date_of_birth(minimum_age=30, maximum_age=70)
        department = fake.random_element(
            elements=(
                'Computer Science', 
                'Data Science',
                'Engineering', 
                'Psychology', 
                'Biological Sciences', 
                'Chemistry',
                'Business', 
                'Visual Arts', 
                'English', 
                'Mathematics', 
                'Economics', 
                'Medicine', 
                'Political Science', 
                'Physics'
            )
        )
        annual_salary = round(random.randint(60000, 200000) / 5000) * 5000
        professors.append(
            {
                'id': id,
                'title': title,
                'first_name': first_name,
                'last_name': last_name,
                'gender': gender,
                'address': address,
                'date_of_birth': date_of_birth,
                'department': department,
                'annual_salary': annual_salary
            }
        )
    return professors


def get_random_course() -> dict:
    response = requests.get(f'http://localhost:8000/courses/', headers={'accept': 'application/json'})
    data = response.json()
    existing_ids = [record['id'] for record in data]
    id = None
    while id in existing_ids or id is None:
        department_code = random.choice(config.departments)
        response = requests.get(f'https://web-app.usc.edu/web/soc/api/classes/{department_code}/20241')
        data = response.json()
        idx = random.randint(0, len(data['OfferedCourses']['course'])-1)
        id = data['OfferedCourses']['course'][idx]['PublishedCourseID']

    department = data.get('Dept_Info').get('department')
    name = data['OfferedCourses']['course'][idx]['CourseData']['title']
    units = int(float(data['OfferedCourses']['course'][idx]['CourseData']['units']))
    return {
        'id': id,
        'name': name,
        'units': units,
        'department': department
    }

def generate_random_courses(n: int) -> list[dict]:
    fake = Faker()
    courses = []
    for i in range(0, n):
        department_code = random.choice(config.departments)
        response = requests.get(f'https://web-app.usc.edu/web/soc/api/classes/{department_code}/20241')
        if response.status_code != 200:
            raise Exception(f'API call failed with status code: {response.status_code}')
        data = response.json()
        department = data.get('Dept_Info').get('department')
        id = data['OfferedCourses']['course'][random.randint(0, len(data['OfferedCourses']['course'])-1)]['PublishedCourseID']
        name = None
        units = random.choices([1, 2, 3, 4], weights=[1, 5, 15, 20])

        courses.append(
            {
                'id': id,
                'name': name,
                'units': units,
                'department': department
            }
        )