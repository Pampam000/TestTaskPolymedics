from datetime import date

from pydantic import BaseModel, Field, validator

from app.config import MIN_STUDENT_AGE


class Base(BaseModel):
    name: str = Field(default=None, max_length=50)
    birthdate: date = None
    group_id: int = Field(default=None, ge=1)

    @validator('birthdate')
    def check_age(cls, value):
        if value:
            age = (date.today() - value).days // 365
            if age < MIN_STUDENT_AGE:
                raise ValueError(f'Age must be greater than {MIN_STUDENT_AGE}')
            return value


class BaseStudent(Base):
    name: str = Field(..., max_length=50)
    birthdate: date
    group_id: int = Field(..., ge=1)


class GraduatedStudent(BaseModel):
    is_graduated: bool = False


class ExpelledStudent(BaseModel):
    is_expelled: bool = False


class Student(BaseStudent, GraduatedStudent, ExpelledStudent):
    pass


class UpdateStudent(Base, GraduatedStudent, ExpelledStudent):
    pass


class StudentId(Student):
    id: int

class UpdateStudentId(UpdateStudent):
    id: int