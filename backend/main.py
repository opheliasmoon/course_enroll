from fastapi import FastAPI
from database import engine
import models

from routers import courses, enrollments, grades, instructors, schedules

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CourseEnroll System")

app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(grades.router)
app.include_router(instructors.router)
app.include_router(schedules.router)


