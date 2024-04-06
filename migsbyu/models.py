from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Double
from sqlalchemy.orm import relationship

from .database import Base



class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    address = Column(String)
    date_of_birth = Column(Date)
    major = Column(String)
    year_of_study = Column(Integer)
    gpa = Column(Double)
    enrollment_status = Column(String)


class Professor(Base):
    __tablename__ = 'professors'

    id = Column(String, primary_key=True)
    title = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    address = Column(String)
    department = Column(String)
    date_of_birth = Column(Date)
    annual_salary = Column(Integer)


class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True)
    name = Column(String)
    units = Column(Integer)
    department = Column(String)


# class Takes(Base):
#     __tablename__ = 'takes'

#     student_id = Column(String, ForeignKey('students.id'))
#     course_id = Column(String, ForeignKey('courses.id'))
#     semester = Column(String)


# class Teaches(Base):
#     __tablename__ = 'teaches'

#     professor_id = Column(String, ForeignKey('professors.id'))
#     course_id = Column(String, ForeignKey('courses.id'))
#     semester = Column(String)