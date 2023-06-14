from fastapi import FastAPI

from .course.routes import router as course_router
from .grade.routes import router as grade_router
from .student.routes import router as student_router
from .teacher.routes import router as teacher_router

app = FastAPI()
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)
app.include_router(grade_router)


@app.get('/')
async def root():
    return {"— Yoda, are you sure we're headed in the right direction?":
            "— Off course we are"}
