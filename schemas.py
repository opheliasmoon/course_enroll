from pydantic import BaseModel
import datetime


# -------- COURSE --------
class CourseCreate(BaseModel):
    CourseName: str
    Credits: int
    Department: str


# -------- ENROLLMENT --------
class EnrollmentCreate(BaseModel):
    StudentID: int
    CourseID: int


# -------- GRADE --------
class GradeCreate(BaseModel):
    StudentID: int
    CourseID: int
    InstructorID: int
    GradeValue: str


# -------- SCHEDULE --------
class ScheduleCreate(BaseModel):
    CourseID: int
    InstructorID: int
    RoomNumber: str
    DayOfWeek: str
    StartTime: datetime.time
    EndTime: datetime.time

