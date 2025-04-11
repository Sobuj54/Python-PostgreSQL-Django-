class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []  # list of student objects
        self.subjects = []  #list of subject objects

    def add_student(self, student):
        roll = len(self.students)
        student.id = roll
        self.students.append(student)
    
    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        
        for student in self.students:
            student.calculate_final_grade()
