from asyncpg import ForeignKeyViolationError, Connection, Record
from fastapi import APIRouter, HTTPException, Body, Path, Depends

from app import db
from app.student.schemas import StudentId
from . import crud, data_examples
from .exceptions import Course404
from .schemas import BaseCourse, CourseWithProgram

router = APIRouter(prefix='/courses', tags=['Courses'])


@router.post('/', status_code=201, response_model=BaseCourse)
async def create_course(
        course: BaseCourse = Body(examples=data_examples.course_example),
        conn: Connection = Depends(db.get_connection)) -> BaseCourse:
    """
    # Create new course

    ## Arguments:
    - `title`: str, required, max length = 50
    - `duration_in_hours`: int, required,  20 <= value <= 200
    - `teacher_id`: int, required, 1 <= value
    - `study_plan_id`: int, optional, 1 <= value
    """
    try:
        await crud.create_course(conn=conn, course=course)
    except ForeignKeyViolationError as e:
        raise HTTPException(status_code=404, detail=e.detail)

    return course


@router.get('/{course_id}', response_model=CourseWithProgram)
async def get_course(
        course_id: int = Path(..., ge=1),
        conn: Connection = Depends(db.get_connection)) -> CourseWithProgram:
    if course := await crud.get_course(conn=conn, course_id=course_id):
        return course

    raise Course404(course_id=course_id)


@router.get('/{course_id}/students', response_model=list[StudentId])
async def get_course_students(
        course_id: int = Path(..., ge=1),
        conn: Connection = Depends(db.get_connection)) -> list[StudentId]:
    result: list[Record] = await crud.get_course_students(conn=conn,
                                                          course_id=course_id)
    if result is None:
        raise Course404(course_id=course_id)

    return result
