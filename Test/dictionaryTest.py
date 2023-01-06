'''
Created on 2023. 1. 4.

@author: kdkin
'''

class CoffeeMaker:

    def __init__(self): 
        self.resource = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    
    def report(self):
        return self.resource        

cf = CoffeeMaker()
print(cf.resource.index[0])
  