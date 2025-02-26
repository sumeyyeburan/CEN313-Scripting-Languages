class StudentGrades():

    def __init__(self):
        self.students=[]

    def addStudent(self,name,grade):
        self.students.append((name,grade))

    def __iter__(self):
        for name,grade in self.students:
            if grade >=50 :
                yield name

s=StudentGrades()

s.addStudent("Sumeyye",30)
s.addStudent("Ahmet",70)
s.addStudent("Melike",50)
s.addStudent("Nisa",80)
s.addStudent("Zeki",45)

for i in s:
    print(i)
