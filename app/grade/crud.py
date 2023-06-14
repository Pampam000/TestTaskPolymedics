from asyncpg import Connection

from .schemas import StudentCourseGrade, Grade


async def create_student_course_grade(
        conn: Connection,
        student_course_grade: StudentCourseGrade):
    """
    Table 'StudentExamGrade' is auto-completed (Look at create_triggers.sql)
    so we need to update data instead of insert new one
    """
    result: str = await conn.execute(
        """
        UPDATE StudentExamGrade 
        SET grade_value =$1
        WHERE student_id=$2 AND exam_id
        IN (SELECT id FROM Exam WHERE course_id=$3)
        """,
        student_course_grade.grade_value,
        student_course_grade.student_id,
        student_course_grade.course_id)
    return result


async def update_student_exam_grade(conn: Connection, grade: Grade,
                                    grade_id: int):
    result: str = await conn.execute(
        """
        UPDATE StudentExamGrade 
        SET grade_value =$1
        WHERE id=$2
        """,
        grade.value_,
        grade_id)

    return result
