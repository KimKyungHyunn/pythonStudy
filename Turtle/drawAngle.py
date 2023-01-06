'''
Created on 2023. 1. 5.

@author: kdkin
'''
from turtle import Turtle, Screen
import random

turtle = Turtle()

colorList = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "SeaGreen"]

for i in range(3, 12, 1):
    angle = 360/i
    count = 0
    
    turtle.color(random.choice(colorList))
    turtle.speed(i-2)
    
    while count < i:
        turtle.forward(50)
        turtle.right(angle)
        count += 1


screen = Screen()
screen.exitonclick()