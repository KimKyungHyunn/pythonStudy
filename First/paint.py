'''
Created on 2023. 1. 2.

@author: kdkin
'''
import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil(height * width / cover)
    print(f"You'll new {num_of_cans} cans of paint")
    
    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)