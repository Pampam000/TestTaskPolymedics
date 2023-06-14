from pydantic import BaseModel, Field


class BaseCourse(BaseModel):
    title: str = Field(..., max_length=50)
    duration_in_hours: int = Field(..., ge=20, le=200)
    teacher_id: int = Field(..., ge=1)
    study_plan_id: int = Field(default=None, ge=1)


class CourseId(BaseCourse):
    id: int


class CourseWithProgram(CourseId):
    program: str = None
