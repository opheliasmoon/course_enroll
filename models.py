from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from database import Base


class Student(Base):
    __tablename__ = "students"

    StudentID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Major = Column(String)


class Instructor(Base):
    __tablename__ = "instructors"

    InstructorID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Department = Column(String)


class Course(Base):
    __tablename__ = "courses"

    CourseID = Column(Integer, primary_key=True, index=True)
    CourseName = Column(String)
    Credits = Column(Integer)
    Department = Column(String)


class Enrollment(Base):
    __tablename__ = "enrollments"

    EnrollmentID = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey("students.StudentID"))
    CourseID = Column(Integer, ForeignKey("courses.CourseID"))
    EnrollmentStatus = Column(String)
    EnrollmentDate = Column(Date)


class Grade(Base):
    __tablename__ = "grades"

    GradeID = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey("students.StudentID"))
    CourseID = Column(Integer, ForeignKey("courses.CourseID"))
    InstructorID = Column(Integer, ForeignKey("instructors.InstructorID"))
    GradeValue = Column(String)


class Schedule(Base):
    __tablename__ = "schedules"

    ScheduleID = Column(Integer, primary_key=True)
    CourseID = Column(Integer, ForeignKey("courses.CourseID"))
    InstructorID = Column(Integer, ForeignKey("instructors.InstructorID"))
    RoomNumber = Column(String)
    DayOfWeek = Column(String)
    StartTime = Column(Time)
    EndTime = Column(Time)
