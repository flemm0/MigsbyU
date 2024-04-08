from sqlalchemy.orm import Session

from . import models, schemas



#region student

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

def delete_student(db: Session, student_id: str):
    db.query(models.Student).filter(models.Student.id == student_id).delete()
    db.commit()
    return

# endregion


# region professors

def create_professor(db: Session, professor: schemas.ProfessorCreate):
    new_prof = models.Professor(**professor.model_dump())
    db.add(new_prof)
    db.commit()
    db.refresh(new_prof)
    return new_prof


def get_professor_by_id(db: Session, professor_id: str):
    return db.query(models.Professor).filter(models.Professor.id == professor_id).first()


def get_professors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Professor).offset(skip).limit(limit).all()


def update_professor(db: Session, professor_id: str, professor: schemas.ProfessorCreate):
    db_prof = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    for attr, val in professor.model_dump().items():
        setattr(db_prof, attr, val)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def delete_professor(db: Session, professor_id: str):
    db.query(models.Professor).filter(models.Professor.id == professor_id).delete()
    db.commit()
    return

# endregion


# region courses

def create_course(db: Session, course: schemas.CourseCreate):
    new_course = models.Course(**course.model_dump())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


def get_course_by_id(db: Session, course_id: str):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def update_course(db: Session, course_id: str, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id == course.id).first()
    for attr, val in course.model_dump().items():
        setattr(db_course, attr, val)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: str):
    db.query(models.Course).filter(models.Course.id == course_id).delete()
    db.commit()
    return

# endregion