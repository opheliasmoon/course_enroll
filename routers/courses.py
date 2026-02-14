from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# View Course List
@router.get("/")
def view_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()


# Add Course
@router.post("/")
def add_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    return new_course


# Update Course
@router.put("/{course_id}")
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.CourseID == course_id).first()
    for key, value in course.dict().items():
        setattr(db_course, key, value)
    db.commit()
    return db_course


# Delete Course
@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.CourseID == course_id).first()
    db.delete(course)
    db.commit()
    return {"message": "Course deleted"}
