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