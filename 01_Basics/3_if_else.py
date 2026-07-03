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

#example 
weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi<18.5:
    print("underweight")
elif bmi<25:
        print("normal weight")
else:
        print("overweight")


#multiple if statement
 
print("welcome to roller coster ride!")
height=(int(input("what is your height?" )))
bill=0

if height>=120:
    print(" you can ride the roller coaster")

    age=(int(input("what is ur age?")))
    if age<=12:
        bill=5
        print("child ticket are 5$")
    elif age<=18:
        bill=12
        print("youth ticket are 12$")
    else:
        bill=20
        print("adult ticket are 20$")

    want_photos=input("do u want photos? type'y' for yes and 'n' for no: ")
    if want_photos=="y":
        bill+=3
    print(f"ur final bill is {bill}")
else:
    print("u cant ride")
 
###example of pizza order using if,elif, multiple if....

print("welcome to the pizza hut!")
size=input("what size do u want ?type 's' for small  'm'for medium  'l'for large :")
pepperoni=input("do u want pepperoni on pizza? y or n :")
extra_cheese=input("do u want cheese on pizza? y or n :")
#size
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif  size=="l":
    bill+=25
else:
    print("u type the wrong input...")

#pepperoni
if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3

#cheese
if extra_cheese=="y":
    bill+=1

print(f"your final boll is{bill} :")

###logical operator
print("welcome to roller coster ride!")
height=(int(input("what is your height?" )))
bill=0

if height>=120:
    print(" you can ride the roller coaster")

    age=(int(input("what is ur age?")))
    if age<=12:
        bill=5
        print("child ticket are 5$")
    elif age<=18:
        bill=12
        print("youth ticket are 12$")
    elif age>=45 and age<=55:   ####logic operator 2 condition     
        print("have a free ride")
    else:
        bill=20
        print("adult ticket are 20$")

    want_photos=input("do u want photos? type'y' for yes and 'n' for no: ")
    if want_photos=="y":
        bill+=3
    print(f"ur final bill is {bill}")
else:
    print("u cant ride")
 