from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/schedules", tags=["Schedules"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add Schedule
@router.post("/")
def add_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    new_schedule = models.Schedule(**schedule.dict())
    db.add(new_schedule)
    db.commit()
    return new_schedule


# Update Schedule
@router.put("/{schedule_id}")
def update_schedule(schedule_id: int, schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = db.query(models.Schedule).filter(models.Schedule.ScheduleID == schedule_id).first()
    for key, value in schedule.dict().items():
        setattr(db_schedule, key, value)
    db.commit()
    return db_schedule


# Delete Schedule
@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Schedule).filter(models.Schedule.ScheduleID == schedule_id).first()
    db.delete(record)
    db.commit()
    return {"message": "Schedule deleted"}


# View Schedule
@router.get("/")
def view_schedule(db: Session = Depends(get_db)):
    return db.query(models.Schedule).all()
