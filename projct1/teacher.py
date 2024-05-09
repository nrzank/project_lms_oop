from user import User


class Submission:
    def __init__(self, assignment, status, grade):
        self.assignment = assignment
        self.status = status
        self.grade = grade


def grade_submission(submission, grade):
    submission.grade = grade
    print(f"Оценка {grade} выставлена для задания {submission.assignment.title}")


def grade_assignment(student, assignment, grade):

    for submission in student.submissions:
        if submission.assignment == assignment:
            submission.grade = grade
            print(f"Оценка {grade} выставлена для студента {student.name} по заданию {assignment.title}")


class Teacher(User):
    def __init__(self, name, email, teacher_id):
        super().__init__(name, email)
        self.teacher_id = teacher_id
        self.assignments = []


    def display_info(self):
        print(f"Имя учителя: {self.name}, Электронная почта: {self.email}, Номер учителя: {self.teacher_id}")



    @staticmethod
    def grade_assignment(student, assignment, grade):

        for submission in student.submissions:
            if submission.assignment == assignment:
                submission.grade = grade
                print(f"Оценка {grade} выставлена для студента {student.name} по заданию {assignment.title}")


    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Задание {assignment.title} добавлено учителю {self.name}")



    @staticmethod
    def grade_submission(submission, grade):
        submission.grade = grade
        print(f"Оценка {grade} выставлена для задания {submission.assignment.title}")
