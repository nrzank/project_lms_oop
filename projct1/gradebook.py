
class GradeBook:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, assignment, grade):
        if student.student_id not in self.grades:
            self.grades[student.student_id] = {}
        self.grades[student.student_id][assignment.title] = grade

    def display_grades(self, student):
        if student.student_id in self.grades:
            print(f"Оценки для студента {student.name}: {self.grades[student.student_id]}")
        else:
            print("Студент еще не получил оценок")

    def calculate_average_grade(self, student):
        if student.student_id in self.grades:
            grade_list = list(self.grades[student.student_id].values())
            if len(grade_list) > 0:
                average_grade = sum(grade_list) / len(grade_list)
                print(f"Средняя оценка для студента {student.name}: {average_grade}")
            else:
                print("Студент еще не получил оценок")
        else:
            print("Студент еще не получил оценок")
