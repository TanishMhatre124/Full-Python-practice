#methods 

class student:
    college_name="st.john college"
    def __init__(self,name,marks):   # parameter constructor
        self.name=name
        self.marks=marks
        print("what is class?")

    def welcome(self): #method
        print("welcome to the python programming :",self.name )    #self.name → ✅ Attribute (instance variable)

s1=student("tan",100)   #← Create object
print(s1.name,s1.marks)
#first create the object than call the method 
s1.welcome()       # ← Call method

#example 

#question - Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

#solution
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks 
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hii",self.name,"your average score is:",sum/3)
        
s1=student("rahul",[100,90,60])
print(s1.name)
s1.get_avg()