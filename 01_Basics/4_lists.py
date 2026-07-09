#rondom module

import random

random_integer=random.randint(1,10) 
print(random_integer)

#2
import  random

random_no_0_t0_1=random.random()*10   # print b/w 1 to 10
print(random_no_0_t0_1)  

#3
import  random

random_float=random.uniform(1,10) #include lower & uppaer bound as well
print(random_float)    

#4-heads tails random print
import random
random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
    print("heads")
else:
    print("tails")

####lists
states_of_america=["washinton","nework","newjersey","alaska"]

#1-print 1 list
states_of_america=["washinton","nework","newjersey","alaska"]
print(states_of_america[0])

#2-change name of list
states_of_america=["washinton","nework","newjersey","alaska"]
states_of_america[1] ="wash"
print(states_of_america)

#3-print random name from list
import random
friends=("tanish","parth","tejas","prince")
print(random.choice(friends)) #option 1

random_index=random.randint(0,4)
print(friends[random_index]) #option 2

#4-nested list

dirty_dozen= ["Apple", "Banana", "Mango", "Orange", "Grapes","Pineapple", "Watermelon", "Papaya", "Strawberry", "Kiwi","Potato", "Tomato", "Onion", "Carrot", "Cabbage","Cauliflower", "Spinach", "Broccoli", "Brinjal", "Peas","Radish","Beetroot","Pumpkin", "Bitter Gourd", "Bottle Gourd","Lady Finger", "Capsicum", "Corn", "Cucumber", "Turnip"]

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes","Pineapple", "Watermelon", "Papaya", "Strawberry", "Kiwi"]
vegetables = ["Potato", "Tomato", "Onion", "Carrot", "Cabbage","Cauliflower", "Spinach", "Broccoli", "Brinjal", "Peas","Radish","Beetroot","Pumpkin", "Bitter Gourd", "Bottle Gourd","Lady Finger", "Capsicum", "Corn", "Cucumber", "Turnip"]

dirty_dozen=[fruits,vegetables]
print(dirty_dozen)



#miniproject
#rock paper scissors game 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper, scissors]
users_choice=int(input("what do u choose ? type 0 for rock , 1 for paper , 2 for scossor: \n"))

if users_choice>=0 and users_choice<=2:
    print(game_images[users_choice])

computer_choice=random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])

if users_choice>=3 or users_choice<0:
    print("u type invalid number.you lose!")
elif users_choice==0 and computer_choice==2:
    print("you wins!")
elif computer_choice==0 and users_choice==2:
    print("you lose!")
elif computer_choice>users_choice:
    print("you loose!")
elif users_choice>computer_choice:
    print(" u win")
elif computer_choice==users_choice:
    print("its a draw!")



