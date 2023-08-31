import random
import sqlalchemy

from database.db import session
from database.models import Group, Mark, Student, Subject, Teacher
from seed import GROUPS, HOW_MANY_TEACHERS, HOW_MANY_STUDENTS, SUBJECTS

TEACHERS_ID = [id_ for id_ in range(1, HOW_MANY_TEACHERS + 1)]
STUDENTS_ID = [id_ for id_ in range(1, HOW_MANY_STUDENTS + 1)]


def select_1():
    """
    Найти 5 студентов с наибольшим средним баллом по всем предметам.
    """

    top_students = session.query(Student.name, sqlalchemy.func.avg(Mark.mark).label('average_mark'))\
        .join(Mark, Student.id == Mark.student_id)\
        .group_by(Student.id)\
        .order_by(sqlalchemy.func.avg(Mark.mark).desc())\
        .limit(5)\
        .all()

    for student_name, average_mark in top_students:
        print(f'Students: {student_name}, Average Mark: {round(average_mark, 2)}')


def select_2(subject: str = random.choice(SUBJECTS)):
    """
    Найти студента с наибольшим средним баллом по определенному предмету.
    """

    if subject not in SUBJECTS:
        print('There is no such subject in the database')
        return

    sub_query = session.query(Student.id, sqlalchemy.func.avg(Mark.mark).label('average_mark'))\
        .join(Mark, Student.id == Mark.student_id)\
        .join(Subject, Mark.subject_id == Subject.id)\
        .filter(Subject.name == subject).group_by(Student.id)\
        .subquery()

    result = session.query(Student, sub_query.c.average_mark)\
        .join(sub_query, Student.id == sub_query.c.id)\
        .order_by(sub_query.c.average_mark.desc())\
        .first()

    top_student, average_mark = result
    print(f'Top Student for {subject}: {top_student.name}, Average Mark: {round(average_mark)}')


def select_3(subject: str = random.choice(SUBJECTS)):
    """
    Найти средний балл в группах по определенному предмету.
    """

    if subject not in SUBJECTS:
        print('There is no such subject in the database')
        return

    result = session.query(Group.name.label('group_name'), sqlalchemy.avg(Mark.mark).label('average_mark'))\
        .join(Student, Group.id == Student.group_id)\
        .join(Mark, Student.id == Mark.student_id)\
        .join(Subject, Mark.subject_id == Subject.id)\
        .filter(Subject.name == subject)\
        .group_by(Group.name)\
        .all()

    print(f'For {subject}:')

    for group_name, average_mark in result:
        print(f'For {group_name} average mark: {round(average_mark, 2)}')


def select_4():
    """
    Найти средний балл на потоке (по всей таблице оценок).
    """

    average_mark = session.query(sqlalchemy.func.avg(Mark.mark)).scalar()
    print(f'Average Mark Overall: {round(average_mark, 2)}')


def select_5(teacher_id: int = random.choice(TEACHERS_ID)):
    """
    Найти какие курсы читает определенный преподаватель.
    """

    if teacher_id not in TEACHERS_ID:
        print('There is no such teacher in the database')
        return

    courses = session.query(Subject.name)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id)\
        .all()

    target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()

    if courses:
        print(f'Courses taught by {target_teacher.name}:')

        for course in courses:
            print(course.name)

    else:
        print(f'This teacher {target_teacher.name} is a slacker, he has no subjects to teach')

    print(f'\nTeacher ID: {teacher_id}')


def select_6(group_name: str = random.choice(GROUPS)):
    """
    Найти список студентов в определенной группе.
    """

    if group_name not in GROUPS:
        print('There is no such group in the database')
        return

    students_in_group = session.query(Student).join(Group).filter(Group.name == group_name).all()

    print(f'List of students in the {group_name}:')

    for student in students_in_group:
        print(student.name)


def select_7(group_name: str = random.choice(GROUPS), subject_name: str = random.choice(SUBJECTS)):
    """
    Найти оценки студентов в отдельной группе по определенному предмету.
    """

    if group_name not in GROUPS:
        print('This group is not in the database')
        return

    elif subject_name not in SUBJECTS:
        print('This subject is not in the database')
        return

    marks_in_group_subject = session.query(Student.name, Mark.mark)\
        .join(Group)\
        .join(Mark)\
        .join(Subject)\
        .filter(Group.name == group_name)\
        .filter(Subject.name == subject_name)\
        .all()

    print(f'Students grades in the {group_name} in the subject {subject_name}:')

    for student_name, mark in marks_in_group_subject:
        print(f'{student_name}: {mark}')


def select_8(teacher_id: int = random.choice(TEACHERS_ID)):
    """
    Найти средний балл, который ставит определенный преподаватель по своим предметам.
    """

    average_mark = session.query(sqlalchemy.func.avg(Mark.mark))\
        .join(Subject)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id)\
        .scalar()

    target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()

    if average_mark is not None:
        print(f'Average grade point average og the teacher {target_teacher.name}: {round(average_mark, 2)}')

    else:
        print(f'This teacher {target_teacher.name} is a slacker, he has no subjects to teach')

    print(f'\nTeacher ID: {teacher_id}')


def select_9(student_id: int = random.choice(STUDENTS_ID)):
    """
    Найти список курсов, которые посещает студент.
    """

    if student_id not in STUDENTS_ID:
        print('There are vo such student id in the database')
        return

    courses_attended = session.query(Subject.name)\
        .join(Mark)\
        .join(Student)\
        .filter(Student.id == student_id)\
        .distinct()\
        .all()

    target_student = session.query(Student).filter_by(id=student_id).first()

    print(f'List of courses attended by the student {target_student.name}:')

    for course in courses_attended:
        print(course.name)

    print(f'\nStudent ID: {student_id}')


def select_10(teacher_id: int = random.choice(TEACHERS_ID), student_id: int = random.choice(STUDENTS_ID)):
    """
    Список курсов, которые студенту читает определенный преподаватель.
    """

    if student_id not in STUDENTS_ID:
        print('This student not in the database')
        return

    elif teacher_id not in TEACHERS_ID:
        print('This teacher not in the database')
        return

    courses_attended_by_student = session.query(Subject.name)\
        .join(Mark, Mark.subject_id == Subject.id)\
        .join(Student, Student.id == Mark.student_id)\
        .join(Teacher, Teacher.id == Subject.teacher_id)\
        .filter(Student.id == student_id)\
        .filter(Teacher.id == teacher_id)\
        .distinct()\
        .all()

    target_student = session.query(Student).filter_by(id=student_id).first()
    target_teacher = session.query(Teacher).filter_by(id=teacher_id).first()

    print(f'A list of courses that student {target_student.name} takes and teacher {target_teacher.name} teaches:')

    for course in courses_attended_by_student:
        print(course.name)

    print(f'Teacher ID: {teacher_id}\nStudent ID: {student_id}')
