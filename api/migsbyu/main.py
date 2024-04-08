from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud

from . import models, schemas
from .database import SessionLocal, engine



app = FastAPI(root_path='/', docs_url='/')


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


tags_metadata = [
    {
        'name': 'students',
        'description': 'Operations with students. List all students, get a student\'s information by id, add new student, or update existing student\'s info.'
    },
    {
        'name': 'professors',
        'description': 'Operations with professors. List all professors, get a professor\s information by id, add new professor, or update existing professor\'s info.'
    },
    {
        'name': 'courses',
        'description': 'Operations with courses. List all courses, get course information by its id, add new course, or update existing course\'s info.'
    }
]


# region students

@app.post('/students/', response_model=schemas.Student, tags=['students'])
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = crud.get_student_by_id(db, student_id=student.id)
    if new_student:
        raise HTTPException(status_code=400, detail='Student already registered')
    return crud.create_student(db=db, student=student)


@app.get('/students/{student_id}', response_model=schemas.Student, tags=['students'])
def get_student(student_id: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student


@app.get('/students/', response_model=list[schemas.Student], tags=['students'])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.put('/students/{student_id}', response_model=schemas.Student, tags=['students'])
def update_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing_student = crud.get_student_by_id(db, student_id=student.id)
    if not existing_student:
        raise HTTPException(status_code=400, detail='Student id not registered')
    return crud.update_student(db=db, student_id=student.id, student=student)


@app.delete('/students/{student_id}', tags=['students'])
def delete_student(student_id: str, db: Session = Depends(get_db)):
    existing_student = crud.get_student_by_id(db=db, student_id=student_id)
    if not existing_student:
        raise HTTPException(status_code=400, detail='Student id not registered')
    else:
        crud.delete_student(db=db, student_id=student_id)
        return {'ok': True}

# endregion


# region professors

@app.post('/professors/', response_model=schemas.Professor, tags=['professors'])
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    new_professor = crud.get_professor_by_id(db, professor_id=professor.id)
    if new_professor:
        raise HTTPException(status_code=400, detail='Professor already registered')
    return crud.create_professor(db=db, professor=professor)


@app.get('/professors/{professor_id}', response_model=schemas.Professor, tags=['professors'])
def get_professor(professor_id: str, db: Session = Depends(get_db)):
    professor = crud.get_professor_by_id(db, professor_id=professor_id)
    if professor is None:
        raise HTTPException(status_code=404, detail='Professor not found')
    return professor


@app.get('/professors/', response_model=list[schemas.Professor], tags=['professors'])
def get_professors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    professors = crud.get_professors(db, skip=skip, limit=limit)
    return professors


@app.put('/professors/{professor_id}', response_model=schemas.Professor, tags=['professors'])
def update_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    existing_professor = crud.get_professor_by_id(db, professor_id=professor.id)
    if not existing_professor:
        raise HTTPException(status_code=400, detail='Professor id not registered')
    return crud.update_professor(db=db, professor_id=professor.id, professor=professor)


@app.delete('/professors/{professor_id}', tags=['professors'])
def delete_professor(professor_id: str, db: Session = Depends(get_db)):
    existing_professor = crud.get_professor_by_id(db=db, professor_id=professor_id)
    if not existing_professor:
        raise HTTPException(status_code=400, detail='Professor id not registered')
    else:
        crud.delete_professor(db=db, professor_id=professor_id)
        return {'ok': True}

# endregion


# region courses

@app.post('/courses/', response_model=schemas.Course, tags=['courses'])
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = crud.get_course_by_id(db, course_id=course.id)
    if new_course:
        raise HTTPException(status_code=400, detail='Course already registered')
    return crud.create_course(db=db, course=course)


@app.get('/courses/{course_id}', response_model=schemas.Course, tags=['courses'])
def get_course(course_id: str, db: Session = Depends(get_db)):
    course = crud.get_course_by_id(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return course


@app.get('/courses/', response_model=list[schemas.Course], tags=['courses'])
def get_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@app.put('/courses/{course_id}', response_model=schemas.Course, tags=['courses'])
def update_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    existing_course = crud.get_course_by_id(db, course_id=course.id)
    if not existing_course:
        raise HTTPException(status_code=400, detail='Course id is not registered')
    return crud.update_course(db=db, course_id=course.id, course=course)


@app.delete('/courses/{course_id}', tags=['courses'])
def delete_course(course_id: str, db: Session = Depends(get_db)):
    existing_course = crud.get_course_by_id(db=db, course_id=course_id)
    if not existing_course:
        raise HTTPException(status_code=400, detail='Course id not registered')
    else:
        crud.delete_course(db=db, course_id=course_id)
        return {'ok': True}

# endregion