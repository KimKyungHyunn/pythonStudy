'''
Created on 2023. 1. 5.

@author: kdkin
'''
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    
    return random_color
    
turtle.pensize(10)
turtle.speed(10)

# for _ in range(100):
#     turtle.color(random_color())
#     turtle.circle(100)  

for _ in range(200):
    turtle.color(random_color())
    turtle.forward(50)
    i = random.randrange(1,5)
    turtle.right(90*i)
    

screen = t.Screen()
screen.exitonclick()