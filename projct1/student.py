from user import User


class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
        self.assigments = []


    def display_info(self):
        print(f"Имя студента: {self.name}, Электронная почта: {self.email}, Номер студента: {self.student_id}")


    def submit_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' submitted by student {self.name}.")


    def view_grades(self):
        for assignment in self.assignments:
            print(f"Assignment: {assignment.title}, Grade: {assignment.grade}")


    def view_average_grade(self):
        if not self.assignments:
            print("No assignments submitted.")
            return
