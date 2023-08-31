import random

from faker import Faker

from database.db import session
from database.models import Group, Mark, Student, Subject, Teacher


fake = Faker()
GROUPS = ('Group A', 'Group B', 'Group C')
SUBJECTS = ('Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Computer Science')
HOW_MANY_TEACHERS = 5
HOW_MANY_STUDENTS = 50


def create_groups():
    for name_group in GROUPS:
        group = Group(name=name_group)
        session.add(group)

    session.commit()


def create_students():
    groups = session.query(Group).all()

    for _ in range(HOW_MANY_STUDENTS):
        group = random.choice(groups)
        student = Student(name=fake.name(), group_id=group.id)
        session.add(student)

    session.commit()


def create_teachers():
    for _ in range(HOW_MANY_TEACHERS):
        teacher = Teacher(name=fake.name())
        session.add(teacher)

    session.commit()


def create_subjects():
    teachers = session.query(Teacher).all()

    for name_subject in SUBJECTS:
        teacher = random.choice(teachers)
        subject = Subject(name=name_subject, teacher_id=teacher.id)
        session.add(subject)

    session.commit()


def create_marks():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for subject in subjects:
            random_mark = random.randint(1, 12)
            random_date = fake.date_this_year().strftime('%Y.%m.%d')
            mark = Mark(student_id=student.id, subject_id=subject.id, mark=random_mark, date=random_date)
            session.add(mark)

        session.commit()


def make_seed():
    create_groups()
    create_students()
    create_teachers()
    create_subjects()
    create_marks()


if __name__ == '__main__':
    make_seed()
