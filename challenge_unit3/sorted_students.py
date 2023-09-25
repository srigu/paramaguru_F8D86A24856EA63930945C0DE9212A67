class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa
def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students
students=[
    Student('guru',"2k22431",7.8),
    Student('sanjay','2k22443',8.9),
    Student('kulathivel','2k22423',9.1),
    Student('ravi','2k22439',9.9)
    ]
sorted_students=sort_students(students)
for students in sorted_students:
    print("Name:{}. Roll Number{}. CGPA:{}".format(students.name,students.roll_number,students.cgpa))
