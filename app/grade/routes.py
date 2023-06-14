from asyncpg import ForeignKeyViolationError, Connection
from fastapi import APIRouter, Path, HTTPException, Depends

from app import db
from . import crud
from .exceptions import StudentExamGrade404, StudentCourse404
from .schemas import StudentCourseGrade, Grade

router = APIRouter(prefix='/grades', tags=['Grades'])


@router.post('/', status_code=201)
async def create_grade_for_student_in_course(
        student_course_grade: StudentCourseGrade,
        conn: Connection = Depends(db.get_connection)) -> dict:
    """
        # Create grade for student
        ## Arguments:
        - `student_id`: int, required, value > 1
        - `course_id`: int, required, value > 1
        - `grade_value`: int, required, 5 >= value >= 2
    """
    try:
        result: str = await crud.create_student_course_grade(
            conn=conn,
            student_course_grade=student_course_grade)
    except ForeignKeyViolationError as e:
        raise HTTPException(status_code=404, detail=e.detail)

    if '0' in result:  # Example: UPDATE 0
        raise StudentCourse404(student_id=student_course_grade.student_id,
                               course_id=student_course_grade.course_id)

    return student_course_grade


@router.put('/{grade_id}')
async def update_grade(
        grade: Grade,
        grade_id: int = Path(..., ge=1),
        conn: Connection = Depends(db.get_connection)) -> dict:
    try:
        result: str = await crud.update_student_exam_grade(
            conn=conn, grade=grade, grade_id=grade_id)
    except ForeignKeyViolationError as e:
        raise HTTPException(status_code=404, detail=e.detail)

    if '0' in result:  # Example: UPDATE 0
        raise StudentExamGrade404(grade_id=grade_id)

    return {"Message": "Success"}
