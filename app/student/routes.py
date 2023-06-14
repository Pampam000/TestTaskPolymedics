from asyncpg import ForeignKeyViolationError, Connection
from fastapi import APIRouter, HTTPException, Path, Body, Depends

from app import db
from . import crud, data_examples
from .exceptions import Student404
from .schemas import BaseStudent, StudentId, UpdateStudent, Student

router = APIRouter(prefix='/students', tags=['Students'])


@router.post('/', status_code=201, response_model=Student)
async def create_student(
        student: BaseStudent = Body(
            examples=data_examples.student_create_example),
        conn: Connection = Depends(db.get_connection)) -> Student:
    """
        # Create new student

        ## Arguments:
        - `name`: str, required, max length = 50
        - `birthdate`: str, required, age >= 17
        - `group_id`: int, required, value >= 1
    """
    try:
        await crud.create_student(conn=conn, student=student)
    except ForeignKeyViolationError as e:
        raise HTTPException(status_code=404, detail=e.detail)
    return Student(**student.dict())


@router.get('/{student_id}', response_model=StudentId)
async def get_student(
        student_id: int = Path(..., ge=1),
        conn: Connection = Depends(db.get_connection)) -> StudentId:
    if student := await crud.get_student(conn=conn, student_id=student_id):
        return student

    raise Student404(student_id=student_id)


@router.put('/{student_id}')
async def update_student(
        student: UpdateStudent = Body(
            examples=data_examples.student_update_example),
        student_id: int = Path(..., ge=1),
        conn: Connection = Depends(db.get_connection)) -> dict:
    """
    # This PUT-method can also be used as a PATCH one.

    ## Arguments:

    - `name`: str, max length = 50
    - `birthdate`: str, age >= 17
    - `group_id`: int, value >= 1
    - `is_graduated`: bool
    - `is_expelled`: bool

    ## return:
    - `changed fields + id`

    ## All fields are optional but at least one argument must be send
    """
    student = student.dict(exclude_unset=True)
    if not student:
        raise HTTPException(status_code=400,
                            detail="Request body couldn't be empty")

    try:
        result = await crud.update_student(conn=conn, student_id=student_id,
                                           student=student)
    except ForeignKeyViolationError as e:
        raise HTTPException(status_code=404, detail=e.detail)

    if '0' in result:  # Example: UPDATE 0
        raise Student404(student_id=student_id)

    return student | {'id': student_id}


@router.delete('/{student_id}', status_code=204)
async def delete_student(
        student_id: int = Path(ge=1),
        conn: Connection = Depends(db.get_connection)):
    """
        ## Are you sure?

        ![Are you sure?](https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif)
    """

    result = await crud.delete_student(conn=conn, student_id=student_id)
    if '0' in result:  # Example: DELETE 0
        raise Student404(student_id=student_id)
