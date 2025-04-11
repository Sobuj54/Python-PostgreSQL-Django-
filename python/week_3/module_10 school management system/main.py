from school import School
from classroom import ClassRoom
from person import Student, Teacher
from subject import Subject

school = School("abc", "dhaka")

eight = ClassRoom("eight")
nine = ClassRoom("nine")
ten = ClassRoom("ten")

# add classrooms
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# add students
rohim = Student("rohim", eight)
korim = Student("korim", ten)
baten = Student("baten", nine)
rasel = Student("rasel", nine)

school.student_admission(rohim)
school.student_admission(korim)
school.student_admission(baten)
school.student_admission(rasel)

# adding teachers
abul = Teacher("abul")
kabul = Teacher("kabul")
babul = Teacher("babul")
ratul = Teacher("ratul")
# adding subjects
bangla = Subject("bangla", abul)
english = Subject("english", kabul)
math = Subject("math", babul)
ict = Subject("ict", ratul)
physics = Subject("physics", ratul)

eight.add_subject(bangla)
eight.add_subject(english)
nine.add_subject(ict)
nine.add_subject(physics)
ten.add_subject(math)
ten.add_subject(physics)
ten.add_subject(ict)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)
