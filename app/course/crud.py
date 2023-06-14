from asyncpg import Connection, Record

from .schemas import BaseCourse


async def create_course(conn: Connection, course: BaseCourse):
    await conn.fetch(
        '''
        INSERT INTO course 
        (title, duration_in_hours, teacher_id, study_plan_id)
        VALUES ($1, $2, $3, $4);
        ''',
        course.title,
        course.duration_in_hours,
        course.teacher_id,
        course.study_plan_id)


async def get_course(conn: Connection, course_id: int) -> Record | None:
    course: Record | None = await conn.fetchrow(
        '''
        SELECT c.*, cp.description as program FROM course c
        LEFT JOIN courseprogram cp
        ON c.id = cp.course_id WHERE c.id=$1
        ''',
        course_id)

    return course


async def get_course_students(conn: Connection, course_id: int) \
        -> list[Record]:
    course = await conn.fetchrow(
        """
        SELECT id FROM course WHERE id =$1
        """,
        course_id)
    if course:
        students: list[Record] = await conn.fetch(
            """
            SELECT s.* FROM Student s
            JOIN StudyGroup g ON s.group_id = g.id
            JOIN StudyPlan sp ON sp.faculty_title = g.faculty_title
            JOIN course c ON c.study_plan_id = sp.id
            WHERE c.id =$1 ORDER BY s.id;
            """,
            course_id)

        return students

