from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal
import datetime

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Enroll Student
@router.post("/")
def enroll_student(data: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    enrollment = models.Enrollment(
        StudentID=data.StudentID,
        CourseID=data.CourseID,
        EnrollmentStatus="Active",
        EnrollmentDate=datetime.date.today()
    )
    db.add(enrollment)
    db.commit()
    return enrollment


# Drop Course
@router.delete("/{enrollment_id}")
def drop_course(enrollment_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Enrollment).filter(models.Enrollment.EnrollmentID == enrollment_id).first()
    db.delete(record)
    db.commit()
    return {"message": "Enrollment removed"}


# View Enrolled Courses
@router.get("/student/{student_id}")
def view_enrolled_courses(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Enrollment).filter(models.Enrollment.StudentID == student_id).all()


# View Course Availability
@router.get("/availability")
def view_course_availability(db: Session = Depends(get_db)):
    return db.query(models.Course).all()
