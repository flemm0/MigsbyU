from sqlalchemy.orm import Session

from . import models, schemas



def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_student_by_id(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def update_student(db: Session, student_id: str, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    for attr, val in student.model_dump().items():
        setattr(db_student, attr, val)
    db.commit()
    db.refresh(db_student)
    return db_student