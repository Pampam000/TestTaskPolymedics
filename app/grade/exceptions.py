from fastapi import HTTPException

from app.exceptions import Base404





class StudentExamGrade404(Base404):
    key = 'grade_id'
    tablename = 'StudentExamGrade'

    def __init__(self, grade_id: int):
        super().__init__(instance_id=grade_id)


class StudentCourse404(HTTPException):

    def __init__(self, student_id: int, course_id: int):
        super().__init__(
        status_code=404,
        detail=f"Key (student_id)=({student_id}) or/and "
               f"Key (course_id)=({course_id}) not presented"
               f" in tables 'Student' or/and 'Course'")

