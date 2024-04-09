from pydantic import BaseModel
from datetime import date



# region student

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

# endregion


# region professor

class ProfessorBase(BaseModel):
    id: str
    title: str | None = None
    first_name: str
    last_name: str
    gender: str
    address: str
    department: str
    date_of_birth: date
    annual_salary: int


class ProfessorCreate(ProfessorBase):
    pass


class Professor(ProfessorBase):
    class Config:
        from_attributes = True

# endregion


# region course

class CourseBase(BaseModel):
    id: str
    name: str
    units: int
    department: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    class Config:
        from_attributes = True

# endregion