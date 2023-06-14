from app.exceptions import Base404


class Course404(Base404):
    key = 'course_id'
    tablename = 'Course'

    def __init__(self, course_id: int):
        super().__init__(instance_id=course_id)
