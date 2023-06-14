from asyncpg import Connection, Record

from .schemas import BaseStudent


async def get_student(conn: Connection, student_id: int) -> Record:
    student: Record = await conn.fetchrow(
        'SELECT * FROM student WHERE id=$1',
        student_id)

    return student


async def create_student(conn: Connection, student: BaseStudent):
    await conn.execute(
        'INSERT INTO Student (name, birthdate, group_id) VALUES($1, $2, $3)',
        student.name,
        student.birthdate,
        student.group_id)


async def update_student(conn: Connection, student_id: int,
                         student: dict) -> str:
    params_part = ''

    for i, key in enumerate(student):
        params_part += f'{key}=${i + 1}'
        if i < len(student) - 1:
            params_part += ', '
    next_val = len(student.keys()) + 1

    result: str = await conn.execute(
        f'UPDATE student SET {params_part} WHERE id=${next_val}',
        *student.values(),
        student_id)
    return result


async def delete_student(conn: Connection, student_id: int) -> str:
    result: str = await conn.execute(
        'DELETE FROM student WHERE id=$1',
        student_id)
    return result
