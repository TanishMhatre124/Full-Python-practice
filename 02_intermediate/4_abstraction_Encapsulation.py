#Abstraction -------> Hide Implementation (How it works)   
#Encapsulation------>  Hide Data


#🔒 Encapsulation = Keep data + methods together and protect the data.
#🎭 Abstraction = Show only the action (e.g., debit()), hide the implementation (self.balance -= amount).



class accounts:
    def __init__(self,bal,acc):
        self.balance=bal    #balance → Instance variable (or instance attribute)
                            #bal → Parameter
        self.account=acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance =", self.get_balance())


     #credited method
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited ")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance   
    
acc1=accounts(50000,12345)
print(acc1.balance)
print(acc1.account)
acc1.debit(1000)
acc1.credit(500)



#del keyword 

class student:
    def __init__(self,name):
        self.name=name

s1=student("tanish")
print(s1.name)

del s1.name      #del keyword 
print(s1.name)


#private(like) attributes and method 

