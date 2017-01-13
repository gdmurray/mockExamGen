"""
-------------------------------------------------------
multiple_file_gen.py
Generates multiple files at once instead of one
-------------------------------------------------------
Author:  Gregory Murray
ID:      ##########
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-06"
-------------------------------------------------------
"""
from Main import create_questions
import random

CUST_DICT = False
file_questions = []
generated_questions = create_questions()
#CHAPTER 19-22 = 20%
#CHAPTER 23-26 = 20%
#CHAPTER 27-29 = 20%
#CHAPTER 30-32, 35 = 40%
print("""
---------------Welcome to The EC140 Multiple Exam Generator-------------
    - Not for sale
    - do not share this program
------------------------------------------------------------------------

    """)
FILE_AMOUNT = int(input('AMOUNT OF FILES: '))
QUESTIONS_AMOUNT = int(input('QUESTIONS: '))
DIFFICULTY = input('Difficulty (1,2,3,None if random): ')
FILE_TO_WRITE_TO = input('output file: ')


for file_var in range(FILE_AMOUNT):
    fv = open('{}_{}.txt'.format(FILE_TO_WRITE_TO,file_var),'w+',encoding='utf-8')
    
    if DIFFICULTY != "":
        DIFFICULTY = DIFFICULTY.replace(" ", "")
        DIFFICULTY = int(DIFFICULTY)
        CUST_DICT = True
    
    CH19_22_PERC = int(QUESTIONS_AMOUNT * .20)
    CH23_26_PERC = int(QUESTIONS_AMOUNT *.20)
    CH26_29_PERC = int(QUESTIONS_AMOUNT *.20)
    CH30_32_35_PERC = int(QUESTIONS_AMOUNT * .40)
    
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
    fv.write("""
    --------------------------------------------------------------------------------------------------------
    Randomly Generated EC140 Exam
    Questions: {0}
    Difficulty: {1}
    --------------------------------------------------------------------------------------------------------
    
    Your Grade out of ____ / {0}
    
    --------------------------------------------------------------------------------------------------------
    
    """.format(len(file_questions), output_diff))
    count = 1
    for k in file_questions:
        print('Question {}     ______'.format(count), file=fv)
        print('{}'.format(k.question_text),file=fv)
        for line in k.options:
            print('    {}'.format(line),file=fv)
        print("""
        """,file=fv)
        count+=1
    print("""
    --------------------------------------------------------------------------------------------------------
    END OF EXAM
    --------------------------------------------------------------------------------------------------------
    """,file=fv)
    count = 1
    print('Answers: ',file=fv)
    for k in file_questions:
        print("{:>3}. {:>3}".format(count, k.answer),file=fv)
        count +=1
    
    fv.close()
