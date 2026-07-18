#class method 

class person:
    name="virat"

    # def change_name(self,name):
    #     person.name=name         # 1 way Without @classmethod:

    @classmethod
    def change_name(cls,name):      
        cls.name=name                      #With @classmethod:

p1=person()
p1.change_name("rohit sharma")
print(p1.name)
print(person.name) 

#property decorator

class students:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

        # self.percentage=str((self.phy + self.chem + self.math) /3) +"%"

    # def calpercentage(self):
    #     self.percentage=str((self.phy + self.chem + self.math) /3) +"%"
    @property
    def percentage(self):
        return str ((self.phy + self.chem + self.math)/ 3) + "%"

stud1=students(100,90,60)
print(stud1.percentage) 
stud1.phy=86
print(stud1.phy)
# stud1.calpercentage()
# print(stud1.percentage) 
