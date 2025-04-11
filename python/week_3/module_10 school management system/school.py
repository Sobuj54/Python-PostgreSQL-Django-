class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # { "bengali" : teacher_object }
        self.classrooms = {} # { "eight" : classroom_object }

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    def student_admission(self, student):
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return "A+"
        elif marks>=70 and marks<80:
            return "A"
        elif marks>=60 and marks<70:
            return "A-"
        elif marks>=50 and marks<60:
            return "B"
        elif marks>=40 and marks<50:
            return "C"
        elif marks>=30 and marks<40:
            return "D"
        else:
            return "F"
    
    @staticmethod
    def grade_to_value(grade):
        g = {
            "A+" : 5.00,
            "A" : 4.50,
            "A-" : 4.00,
            "B" : 3.50,
            "C" : 3.00,
            "D" : 2.50,
            "F" : 2.00
        }
        return g[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value > 4.50 and value <= 5.00:
            return "A+"
        elif value > 4.00 and value <= 4.50:
            return "A"
        elif value > 3.50 and value <= 4.00:
            return "A-"
        elif value > 3.00 and value <= 3.50:
            return "B"
        elif value > 2.50 and value <= 3.00:
            return "C"
        elif value > 2.00 and value <= 2.50:
            return "D"
        else:
            return "F"
        
    def __repr__(self):
        for key in self.classrooms.keys():
            print(f"class : {key}")

        # all students in all classrooms
        for key,val in self.classrooms.items(): 
            print(f"students of class {key.upper()}")  
            for student in val.students:
                print(f"{student.name}, ")
            print("\n")

        # all subjects in all classrooms
        for key,val in self.classrooms.items(): 
            print(f"students of class {key.upper()}")  
            for sub in val.subjects:
                print(f"{sub.subject}, ")
            print("\n")

        # all student results
        for key,val in self.classrooms.items(): 
            for student in val.students:
                    for k,i in student.marks.items():
                        print(student.name, k, i, student.subject_grade[k])
                    print(student.calculate_final_grade())
            print("\n")
        return ""
        