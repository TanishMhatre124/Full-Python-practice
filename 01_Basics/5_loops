##lops
#1-loop using list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes","Pineapple", "Watermelon", "Papaya", "Strawberry", "Kiwi"]
for fruit in fruits:
    print(fruit)
    print(fruit +"delicious")
print(fruits) 

#2-total score
student_scores = [83, 47, 92, 58, 71, 65, 30, 99, 76, 41,
          88, 54, 67, 39, 95, 62, 73, 81, 46, 60,
          85, 33, 50, 91, 37, 28, 78, 64, 70, 43,
          96, 26, 53, 79, 68, 59, 31, 36, 84, 24,
          55, 98, 44, 82, 66, 32, 75, 61, 40, 90]
total_score=sum(student_scores)# 1 way

#2 way
sum=0
for score in student_scores:
    sum+=score
print(sum)

#3-max score
student_scores = [83, 47, 92, 58, 71, 65, 30, 99, 76, 41,
          88, 54, 67, 39, 95, 62, 73, 81, 46, 60,
          85, 33, 50, 91, 37, 28, 78, 64, 70, 43,
          96, 26, 53, 79, 68, 59, 31, 36, 84, 24,
          55, 98, 44, 82, 66, 32, 75, 61, 40, 90]
max_score=max(student_scores)#1 way

#2 way
max_score=0
for score in student_scores:
    if score > max_score:
        max_score=score
print(max_score)

#4=range function
for numbers in range (1,11,3):
    print(numbers)

#total 
total=0
for numbers in range(1,11):
    total+=numbers
print(total)

#eg
for number in range (1,101):
    print(number)
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
else:
    print(number)


##mini projects
##### password generator
##easy level

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
           ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

print("welcome to the password generator!")
nr_letters=int(input("how many lettrs would u like in your password?\n"))
nr_symbols=int(input("how many symbols would u like in your password?\n"))
nr_numbers=int(input("how many numbers would u like in your password?\n"))

password=""
for char in range(0,nr_letters):
    password +=random.choice(letters)

for char in range(0,nr_symbols):
    password +=random.choice(symbols)

for char in range(0,nr_numbers):
    password +=random.choice(numbers)

print(password)

###hard level

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
           ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

print("welcome to the password generator!")
nr_letters=int(input("how many lettrs would u like in your password?\n"))
nr_symbols=int(input("how many symbols would u like in your password?\n"))
nr_numbers=int(input("how many numbers would u like in your password?\n"))

password_list=[]
for char in range(0,nr_letters):
    password_list+=random.choice(letters)

for char in range(0,nr_symbols):
    password_list +=random.choice(symbols)

for char in range(0,nr_numbers):
    password_list +=random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:  
    password+=char
print(f"your password is:{password}")
 

