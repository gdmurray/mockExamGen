"""
-------------------------------------------------------
in_Console_exam.py
module that lets you do the exam in the console or command line
-------------------------------------------------------
Author:  Gregory Murray
ID:      150236640
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-15"
-------------------------------------------------------
"""
from Main import create_questions
import random

CUST_DICT = False
file_questions = []
generated_questions = create_questions()

print("""
---------------Welcome to The EC140 in Console Exam Simulator----------------------
    - Not for sale
    - do not share this program
------------------------------------------------------------------------

    """)
QUESTIONS_AMOUNT = int(input('QUESTIONS: '))
DIFFICULTY = input('Difficulty (1,2,3,None if random): ')

if DIFFICULTY != "":
    DIFFICULTY = DIFFICULTY.replace(" ", "")
    DIFFICULTY = int(DIFFICULTY)
    CUST_DICT = True

CH19_22_PERC = int(QUESTIONS_AMOUNT * .10)
CH23_26_PERC = int(QUESTIONS_AMOUNT *.10)
CH26_29_PERC = int(QUESTIONS_AMOUNT *.20)
CH30_32_35_PERC = int(QUESTIONS_AMOUNT * .60)

chaps = []
CH1 = [19, 20, 21, 22]
chaps.append(CH1)
CH2 = [23, 24, 25, 26]
chaps.append(CH2)
CH3 = [27, 28, 29, 30]
chaps.append(CH3)
CH4 = [31, 32, 35]
chaps.append(CH4)


for chapter_section in chaps:
    for curr_chapter in chapter_section:
        if curr_chapter in (CH1 or CH2 or CH3):
            per_chapter = int(CH19_22_PERC / 4)
        elif curr_chapter in CH4:
            per_chapter = int(CH30_32_35_PERC / 3)
            
        temp_list = []
        for k in generated_questions:
            if CUST_DICT == True:
                if int(k.chapter) == curr_chapter and int(k.difficulty) == DIFFICULTY:
                    temp_list.append(k)
            else:
                if int(k.chapter) == curr_chapter:
                    temp_list.append(k) 
            
        
        
        #print(len(temp_list))
        
        i = random.sample(range(0,len(temp_list)-1),per_chapter)
            
        for index in i:
            file_questions.append(temp_list[index])
    



#CLOSING FUNCTIONS
if DIFFICULTY == "":
    output_diff = None
else:
    output_diff = DIFFICULTY
    
print(
"""
--------------------------------------------------------------------------------------------------------
Randomly Generated EC140 Exam
Questions: {0}
Difficulty: {1}
--------------------------------------------------------------------------------------------------------

Your Grade out of ____ / {0}

--------------------------------------------------------------------------------------------------------

""".format(len(file_questions), output_diff))

count = 1
answers_right = 0
wrong_questions = []
wrong_ques_num = []
your_answers= []
for k in file_questions:
    print('Question {}     ______'.format(count))
    print('{}'.format(k.question_text))
    for line in k.options:
        print('    {}'.format(line))
    print("""
    """)
    ques_answer = input("Your Answer: ")
    if ques_answer.upper() != k.answer:
        wrong_questions.append(k)
        wrong_ques_num.append(count)
        your_answers.append(ques_answer)
    elif ques_answer == k.answer:
        answers_right += 1   
        your_answers.append(ques_answer)  
    print()   
        
    count+=1

print('End of Exam')
grade = (answers_right / len(file_questions)*100)
print("""
Your Grade is
{0} / {1}  ==  {2:.2f}%)
""".format(answers_right, len(file_questions), grade))

input("Press Enter to See Wrong Answers")
for x in range(len(wrong_questions)):
    print('Question {}     ______'.format(wrong_ques_num[x]))
    print('{}'.format(wrong_questions[x].question_text))
    for line in wrong_questions[x].options:
        print('    {}'.format(line))
    print('Your Answer: {}'.format(your_answers[x]))
    print()
    print('Answer: {}'.format(wrong_questions[x].answer))
    print("""
    """)
