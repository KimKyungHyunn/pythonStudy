'''
Created on 2023. 1. 9.

@author: kdkin
'''

from turtle import Screen

screen = Screen()

class Prompt:
    
    def __init__(self):
        pass
    
    def game_over(self, score):
        answer = screen.textinput(title="game_over", prompt=f"your final score: {score}\nwill you continue? (y or n)")
        
        if answer == "y":
            return True 
        else:
            return False
        
    
    