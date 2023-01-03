'''
Created on 2023. 1. 2.

@author: kdkin
'''

# divisible by 3 = Fizz
# divisible by 5 = Buzz
# both = FizzBuzz

for n in range (1, 101, 1):
    if n%3 == 0 and n%5 ==0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)
        
        
