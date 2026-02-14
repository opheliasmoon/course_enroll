from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/grades", tags=["Grades"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Add Grade
@router.post("/")
def add_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    record = models.Grade(**grade.dict())
    db.add(record)
    db.commit()
    return record


# Update Grade
@router.put("/{grade_id}")
def update_grade(grade_id: int, grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    db_grade = db.query(models.Grade).filter(models.Grade.GradeID == grade_id).first()
    for key, value in grade.dict().items():
        setattr(db_grade, key, value)
    db.commit()
    return db_grade


# Delete Grade
@router.delete("/{grade_id}")
def delete_grade(grade_id: int, db: Session = Depends(get_db)):
    record = db.query(models.Grade).filter(models.Grade.GradeID == grade_id).first()
    db.delete(record)
    db.commit()
    return {"message": "Grade deleted"}


# View Grades
@router.get("/student/{student_id}")
def view_grades(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Grade).filter(models.Grade.StudentID == student_id).all()
