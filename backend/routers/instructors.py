from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal

router = APIRouter(prefix="/instructors", tags=["Instructor Assignments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Assign Instructor (uses schedule as assignment)
@router.post("/assign")
def assign_instructor(course_id: int, instructor_id: int, db: Session = Depends(get_db)):
    assignment = models.Schedule(
        CourseID=course_id,
        InstructorID=instructor_id
    )
    db.add(assignment)
    db.commit()
    return assignment


# Update Instructor Assignment
@router.put("/assign/{schedule_id}")
def update_assignment(schedule_id: int, instructor_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Schedule).filter(models.Schedule.ScheduleID == schedule_id).first()
    record.InstructorID = instructor_id
    db.commit()
    return record


# Remove Instructor
@router.delete("/assign/{schedule_id}")
def remove_assignment(schedule_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Schedule).filter(models.Schedule.ScheduleID == schedule_id).first()
    db.delete(record)
    db.commit()
    return {"message": "Instructor removed"}


# View Assignments
@router.get("/assignments")
def view_assignments(db: Session = Depends(get_db)):
    return db.query(models.Schedule).all()
