from school import School

class Subject:
    def __init__(self, name:str, teacher:object):
        self.subject = name
        self.teacher = teacher
        self.max_mark = 100
        self.pass_mark = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.subject] = mark
            student.subject_grade[self.subject] = School.calculate_grade(mark)