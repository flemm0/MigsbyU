from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    address: str
    date_of_birth: date
    major: str
    year_of_study: int
    gpa: float
    enrollment_status: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True