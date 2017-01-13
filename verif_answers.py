"""
-------------------------------------------------------
verif_answers.py
verifies questions and answers
-------------------------------------------------------
Author:  Gregory Murray
ID:      #########
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-15"
-------------------------------------------------------
"""
from Main import create_questions


generated_questions = create_questions()
run = True

while run:
    question_cont = input('Question Text: ')
    for k in generated_questions:
        if question_cont in k.question_text:
            print(k)
    print("______End of Results_______")
    print()
    print("Next Question")
    print()