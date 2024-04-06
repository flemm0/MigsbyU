from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    id: str
    first_name: str
    last_name: str
    gender: str
    address: str | None = None
    date_of_birth: date
    major: str | None = None
    year_of_study: int
    gpa: float
    enrollment_status: str | None = None


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    class Config:
        from_attributes = True