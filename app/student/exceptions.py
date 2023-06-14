from app.exceptions import Base404


class Student404(Base404):
    key = 'student_id'
    tablename = 'Student'

    def __init__(self, student_id: int):
        super().__init__(instance_id=student_id)
