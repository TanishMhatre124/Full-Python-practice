
#constructor
    
class student:
    name="tanish"
    def __init__(self):   #default constructor
        print(self)
        print("what is your name")
s1=student()
print(s1.name)

#-------------------------------------------------------------------------

class car:
    def __init__(self,fullname):
        self.name=fullname
        print("add new student in database")
s1=car("bmw")
print(s1.name)
#-------------------------------------------------------------------------

class student:
    def __init__(self,name,marks):   # parameter constructor
        self.name=name
        self.marks=marks
        print("what is class?")

s1=student("tan",100)
print(s1.name,s1.marks)

s2=student("jash",90)
print(s2.name,s2.marks)