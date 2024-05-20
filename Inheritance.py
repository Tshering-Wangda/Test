class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year,):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.marks = []

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

    def calculate_gpa(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self, student, marks):
        student.marks.extend(marks)
        print(f"{self.name} graded {student.name}.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")


# Creating objects
student1 = Student("karma", 18, "10203001707", "02230111", "Computer Science", 2)
teacher1 = Teacher("Mr. thinley", 35, "10203001708", "Math", 50000, "Mathematics", "Professor")

# Accessing common attributes and methods
student1.walk()
teacher1.walk()

# Accessing specific attributes and methods
print(student1.student_id)
print(teacher1.subject)

student1.study()
teacher1.teach()

# Using specific methods
teacher1.grade_students(student1, [85, 90, 92])
print(f"{student1.name}'s GPA is {student1.calculate_gpa()}")

student1.write_exam()
teacher1.attend_meeting()