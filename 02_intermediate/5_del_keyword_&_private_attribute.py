
# #del keyword 

class student:
    def __init__(self,name):
        self.name=name

s1=student("tanish")
print(s1.name)

del s1.name      #del keyword 
print(s1.name)

#---------------------------------------------------

#private (like) attributes and method 

class account:
    def __init__(self,acco_no,acc_pass):
        self.account_number=acco_no
        self.__account_pass=acc_pass
    
    def reset_pass(self):
        print(self.__account_pass)

s1=account(924,12345)
print(s1.account_number)
print(s1.reset_pass())

#-----------------------
class person:
    __name="jash"

    def __hello(self):
        print("hello person !")
    
    def welcome(self):
        self.__hello()

p1=person()
print(p1.welcome())