'''
Created on 2023. 1. 6.

@author: kdkin
'''
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:      
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)        
            
    def move(self):
        for seg_num in range (len(self.segments)-1, 0 ,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)   
        self.head.forward(MOVE_DISTANCE)
    
    def clear_snake(self):
        self.__init__()
        
    
    def increase_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def check_conflict(self, headPos):
        for seg_num in range (len(self.segments)-1, 0 ,-1):
            if headPos == self.segments[seg_num-1].position():
                return True
        
        return False    
            
            
    def turn_up(self):
        self.head.setheading(90)
    
    def turn_down(self):
        self.head.setheading(270)
    
    def turn_left(self):
        self.head.setheading(90180)
    
    def turn_right(self):
        self.head.setheading(0)            
            
            
            