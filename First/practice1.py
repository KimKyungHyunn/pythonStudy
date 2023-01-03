'''
Created on 2023. 1. 2.

@author: kdkin
'''
#prac1
#print("hi" + input("input something"))

#prac2
# word = input("insert your name ")
# print(len(word))

#prac3
# numStr = input("insert numStr ")
# first_num = numStr[0]
# second_num = numStr[1]
# result = int(first_num) + int(second_num)
# print(result)

#pract4
# print(8/3)
# print(8//3)
# print(round(8/3 , 2))

#pract5
# a = input("a ")
# if int(a)%2 == 0:
#   print("Â¦¼ö")
# else:
#   print("È¦¼ö")

#pract6
# a = input("a ")
# if int(a) < 5:
#   print("under5")
# elif int(a) < 10:
#   print("under10")
# else:
#   print("upper10")

#pract7
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

count = 0

if size == "S":
    count = 15
elif size == "M":
    count = 20
else:
    count = 25

if add_pepperoni == "Y":
    if size == "S":
        count += 2
    else:
        count += 3

if extra_cheese == "Y":
    count += 1

print("FINAL BILL " + count)

