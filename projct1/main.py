from student import Student
from teacher import Teacher
from course import Course
from assigment import Assignment
from gradebook import GradeBook
from teacher import Submission


def main():
    student1 = Student("Нуржан", "asapnrz@gmail.com", "S001")
    student2 = Student("Бекарыс", "beka@gmail.com", "S002")

    teacher = Teacher("Улан", "ulan@gmail.com", "T001")
    teacher.display_info()
    print('-------------------------')
    course = Course("Python - Разработчик 17", "P001")
    course.add_student(student1)
    course.add_student(student2)
    course.assign_teacher(teacher)
    course.display_info()

    print('--------------------')

    for student in course.students:
        student.display_info()

    print('-------------------------')

    assignment1 = Assignment("Домашнее задание. Практика ООП. 'Библиотека'")
    assignment2 = Assignment('Переопределение методов. Перегрузка операторов.')
    grade_book = GradeBook()
    grade_book.add_grade(student1, assignment1, 90)
    grade_book.add_grade(student1, assignment2, 80)
    grade_book.display_grades(student1)
    grade_book.calculate_average_grade(student1)

    print('-------------------------')
    assignment1 = Assignment("Домашнее задание. Практика ООП. 'Библиотека'")
    assignment2 = Assignment('Переопределение методов. Перегрузка операторов.')
    grade_book = GradeBook()
    grade_book.add_grade(student2, assignment1, 50)
    grade_book.add_grade(student2, assignment2, 76)
    grade_book.display_grades(student2)
    grade_book.calculate_average_grade(student2)
    print('-------------------------')
    teacher.add_assignment(assignment1)
    submission1 = Submission(assignment1, "Submitted", None)
    student1.submissions = [submission1]

    teacher.grade_submission(submission1, 90)
    teacher.grade_assignment(student1, assignment1, 85)


if __name__ == '__main__':
    main()
