class Student:
    def __init__(self,name, id, current_class):
        self.name = name
        self.id = id
        self.current_class = current_class

    # representation is used to print the class
    def __repr__(self):
        return f"student Name:{self.name} id:{self.id}  class:{self.current_class}"

class Teacher:
    def __init__(self,name, id, subject):
        self.name = name
        self.id = id
        self.subject = subject

    # representation is used to print the class
    def __repr__(self):
        return f"teacher Name:{self.name} id:{self.id}  subject:{self.subject}"

class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teachers(self,name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, id, subject)
        self.teachers.append(teacher)

    def enroll_student(self,name,fee):
        if fee < 6500:
             print("not enough fee")
        else:
            id = len(self.students) + 101
            student = Student(name,id,"cse")
            self.students.append(student)
            print(f"student enrolled: {name}  id:{id}") 

    def __repr__(self):
        print(f"welcome to {self.name}\n")
        print("--------our teachers-------------")
        for teacher in self.teachers:
            print(teacher)
        print("\n-------------our students-----------")
        for student in self.students:
            print(student)
        return "end"

# students
# sobuj = Student("Sobuj",21064,"4th year")
# print(sobuj)

# teachers
# toma = Teacher("toma", 555025, "OOP")
# print(toma)


# school
phitron = School("phitron")
phitron.add_teachers("raja", "mara mari")
phitron.add_teachers("kaja", "bara bari")

phitron.enroll_student("kala", 5000)
phitron.enroll_student("pakku", 8000)

print(phitron)