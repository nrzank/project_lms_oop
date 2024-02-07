class Course:
    def __init__(self, title, code):
        self.title = title
        self.code = code
        self.students = []
        self.teacher = None
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def display_info(self):
        print(f"Курс: {self.title}, Код: {self.code}")
        print("Студенты:")
        for student in self.students:
            print(f"Имя студента: {student.name}, Номер студента: {student.student_id}")
        if self.teacher:
            print(f"Учитель: {self.teacher.name}")
        return self
