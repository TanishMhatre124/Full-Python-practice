 #if else statement

print("welcome to thr rollercoaster rider")
height=int(input("what is your height?"))
if height>=120:
    print("you can ride a rollercoaster")
else:
    print("you need to get taller in order to ride")
    

#modulo operator
a=int(input("enter a number:"))
b=2
if a%b==0:
    print("enter number is even")
else:
    print("number is odd ")

#nested if and elif statements  
#1.nested if

print("welcome to the rollercoaster ride!")
height=int(input("what is your height?"))
if height>=120:
    print("you can ride a rollercoaster!")
    age=int(input("kwhat is your age?"))
    if age>=18:
        print("u can ride")
    else:
        print("u need to get taller")
else:
    print("u cant ride a roller coaster")

#2.elif
print("welcome to roller coster ride!")
height=int(input("what is your height?"))
if height >=80:
    print("you can ride roller coster!")
    age=int(input("what is  your age?"))
    
    if age<=12:
        print("please pay 5$...")
    elif age<=18:
            print("please pay 10$...")
    elif age<=24:
            print("please pay 20$...")

    else:
        print("u can take a ride....")
else:
    print("you can't ride roller coster !") 