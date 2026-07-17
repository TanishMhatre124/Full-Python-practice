
from turtle import Turtle ,Screen

timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(180)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


#class and objects 

class student:  #class
    name="bugati"
    color="blue"

s1=student()   #object
print(s1.name)

s2=student()   
print(s2.color)
