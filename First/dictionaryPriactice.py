'''
Created on 2023. 1. 3.

@author: kdkin
'''

student_scores = {
    "Harry": 81,
    "Ran": 91,
    "Json": 72,
    "Drace": 63,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        student_grades[student] = "first"
    elif score > 80:
        student_grades[student] = "second"
    elif score > 70:
        student_grades[student] = "third"    
    else:
        student_grades[student] = "bad"      

print(student_grades)
    
for student in student_grades:
    print(student +":" + student_grades[student])

        
    

