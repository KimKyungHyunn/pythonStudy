'''
Created on 2023. 1. 5.

@author: kdkin
'''
import random
from turtle import Turtle, Screen

turtleDic = [
    {"color":"orange", "y":-180}, 
    {"color":"red", "y":-120}, 
    {"color":"green", "y":-60}, 
    {"color":"blue", "y":0}, 
    {"color":"yellow", "y":60}, 
    {"color":"purple", "y":120},
    {"color":"black", "y":180}
    ]

all_turtles =[]
winner = []

screen = Screen()
# screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle in turtleDic:
    newTurtle = Turtle()
    newTurtle.shape("turtle")
    newTurtle.penup()
    newTurtle.goto(x= -300, y=turtle["y"])
    newTurtle.color(turtle["color"])
    turtleInfo = [newTurtle, turtle["color"]]
    all_turtles.append(turtleInfo)
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtleInfo in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle = turtleInfo[0]
        turtle.forward(rand_distance)
        
        if turtle.xcor() > 300:
            winnerTurtleColor = turtleInfo[1]
            winner.append(winnerTurtleColor)
            all_turtles.remove(turtleInfo)
        
        if len(all_turtles) == 0:
            is_race_on = False       

print(f"winner turtle is {winner[0]} turtle")

if user_bet == winner[0]:
    print("you win")
else:
    print(f"you picked {user_bet}, you loose")

screen.exitonclick()
