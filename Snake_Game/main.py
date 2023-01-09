'''
Created on 2023. 1. 5.

@author: kdkin
'''
from turtle import Screen
from Snake_Game.snake import Snake
from Snake_Game.food import Food
from Snake_Game.scoreboard import Scoreboard
from Snake_Game.prompt import Prompt
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
prompt = Prompt()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)    
    snake.move()
    
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_snake()
       
    
    if snake.head.xcor() <= -300 or snake.head.xcor() >= 300 or snake.head.ycor() <= -300 or snake.head.ycor() >= 300:
        final_score = scoreboard.get_score()
        redo_game = prompt.game_over(final_score)
        
        if redo_game == True:
            game_is_on = True
            scoreboard.refresh_score()
            snake.clear_snake()
            
        else:
            game_is_on = False
            
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
    
    
screen.exitonclick()