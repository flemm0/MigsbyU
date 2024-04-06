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


@app.post('/students/', response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = crud.get_student_by_id(db, student_id=student.id)
    if new_student:
        raise HTTPException(status_code=400, detail='Student already registered')
    return crud.create_student(db=db, student=student)


@app.get('/students/{id}', response_model=schemas.Student)
def get_student(student_id: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student