'''
Created on 2023. 1. 6.

@author: kdkin
'''
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    
    def breathe(self):
        print("In, ex")
        

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def swim(self):
        print("moving in water")
    
    
nemo = Fish()
nemo.swim()    
nemo.breathe()
        