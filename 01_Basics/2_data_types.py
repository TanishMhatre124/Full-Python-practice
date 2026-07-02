#subscripting
print("helo"[1])

print("1.2345")

#datatypes checking

len("hello")

print(type(123))

print(type(1.23))

print(type("123"))

print(type(True))

#type conversion
print(int("123")+int("456"))

name=input("enter your name:")
length_of_name=len(name)
print(type("no. of letters in your name"))
print(type(length_of_name))
print("no. of letter in ur name: " + str(length_of_name))  #enter your name:ksbcxkjn #no. of letter in ur name: 8

#mathematical operations
print("what is my age: " + str("20"))
print(123+456) #add
print(123-321) #sub
print(3*2) #mul
print(5/3) #div
print(5//3) #mod   
print(2**3) #power exponent

#pemdas
"""
P = Parent;pheses
E = Exponents (powers and roots)
M = Multiplication
D = Division
A = Addition
S= Subtraction
"""
print(3*3+3/3-3)   

#bmi calculator
height=505
weight=90
bmi=weight/height**2
print(int(bmi))

#number manipulation
#round
print(round(bmi))
print(round(bmi,2))
#assignment operator 
score=0
score +=1
print(score)

#f-string
score=10
height=5.5
winning_is=True
print(f"your score is: {score},your height is: {height},you are winning: {winning_is}")


#example
print("welcome to the tip calculator!")
total_cost=float(input("what was the total cost of the bill? \n"))
tip=int(input("how much tip should i give to you? 10  ,12 ,15 \n"))
split=int(input("how many people should split the bill ?"))
final_amount=(total_cost+tip)/split
print(f"final payable amount by each person is equal to={final_amount}")