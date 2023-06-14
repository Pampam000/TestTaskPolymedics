from datetime import date

from pydantic import BaseModel, Field, validator

from app.config import MIN_TEACHER_AGE


class TeacherId(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., max_length=50)
    birthdate: date
    classroom_id: int = Field(default=None, ge=1)

    @validator('birthdate')
    def check_age(cls, value):
        if value:
            age = (date.today() - value).days // 365
            if age < MIN_TEACHER_AGE:
                raise ValueError(f'Age must be greater than {MIN_TEACHER_AGE}')
            return value
