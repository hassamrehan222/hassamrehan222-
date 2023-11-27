class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.class_name}.")

    def display_students(self):
        print(f"Students in {self.class_name}:")
        for student in self.students:
            student.display_info()

student1 = Student(name="hassam", grade=12)


classroom1 = Classroom(class_name="Math Class")

classroom1.add_student(student1)

classroom1.display_students()