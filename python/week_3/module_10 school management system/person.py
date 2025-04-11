import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evaluate_exam(self):
        return random.randint(1,100)
    
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}  # { "english" : 80 }
        self.subject_grade = {}  # { "english" : "A+" }
        self.grade = None # final grade

    def calculate_final_grade(self):
        total = 0
        for grade in self.subject_grade.values():
            total += School.grade_to_value(grade)
        gpa = total / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, num):
        self.__id = num