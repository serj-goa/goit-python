from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))


class Mark(Base):
    __tablename__ = 'marks'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    mark = Column(Integer)
    date = Column(String)
