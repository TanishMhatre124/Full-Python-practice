#inheeritance

# single inheritance
class car:
    @staticmethod
    def start():
        print("car started for single inheritance")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):                          #inheritance
    def __init__(self,name):                    
        self.name=name

car1=toyotacar("fortuner")
car2=toyotacar("hyryder")

print(car1.start())



#multiple level inheritance 
class car:
    @staticmethod
    def start():
        print("car started for multiple level inheritance")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):                          #inheritance
    def __init__(self,name):                    
        self.name=name

class fortuner(toyotacar):
    def __init__(self, type):
        self.type=type

car1=fortuner("disel")
car1.start()



#multiple inheritance 

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#-------------------------------------------------------------

#super method

class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started for super method")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):                          #inheritance
    def __init__(self,name,type):                    
        self.name=name
        super().__init__(type)         # #<-----------------------super method to call variable
        super().start()                #<-----------------------super method to call  class

car1=toyotacar("fortuner","electric")

print(car1.start())
print(car1.type)