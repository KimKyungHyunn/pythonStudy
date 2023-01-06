'''
Created on 2023. 1. 4.

@author: kdkin
'''
from Quiz_Game.question_model import Question
from Quiz_Game.data import question_data
from Quiz_Game.quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()    
    
    


    