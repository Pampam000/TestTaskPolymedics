from pydantic import BaseModel, Field


class Grade(BaseModel):
    value_: int


class StudentCourseGrade(BaseModel):
    student_id: int = Field(..., ge=1)
    course_id: int = Field(..., ge=1)
    grade_value: int

