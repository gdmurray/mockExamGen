"""
-------------------------------------------------------
Main.py
module containing the function used to create the questions
-------------------------------------------------------
Author:  Gregory Murray
ID:      ##########
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-02"
-------------------------------------------------------
"""
import re
from Question_Class import Question

def create_questions():
    CHAPTERS = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,35]
    questions = []
    for num in CHAPTERS:
        fv = open('chapter_{}.txt'.format(num),'r+',encoding='utf-8')
        full_doc = fv.readlines()
    
        
        start_locs = []
        end_locs = []
        for x in range(len(full_doc)):
            if x == 0:
                start_locs.append(x)
            if re.match(r'^\s*$', full_doc[x]):
                if len(start_locs) > 0:
                    end_locs.append(x-1)
                    start_locs.append(x+1)
        
        full_question_list = []
        for x in range(len(start_locs)):
            i = start_locs[x]
            temp_list = []
            try:
                while i != end_locs[x]:
                    try:
                        temp_list.append(full_doc[i])
                    except IndexError:
                        break
                    i += 1
                full_question_list.append(temp_list)
            except IndexError:
                continue
            
            
            
        for full_question in full_question_list:
            options = []
            question_text = ""
            x = 0
            try:
                while full_question[x].startswith('A') is False:
                    question_text += full_question[x]
                    x+=1
            except IndexError:
                continue
            while full_question[x].startswith('Answer') is False:
                options.append(full_question[x].strip())
                x+=1
            answer = full_question[x]
            answer = answer[9:10]
            x+=1
            diff = full_question[x]
            diff = diff[6:7]
            if diff == 't':
                diff = 2
            diff = int(diff)
            
            if question_text[1:2] == ')':
                question_text = question_text[3:]
            elif question_text[2:3] == ')':
                question_text = question_text[4:]
            elif question_text[3:4] == ')':
                question_text = question_text[5:]
            chapter = num
            q = Question(question_text=question_text, options=options, answer=answer, difficulty=diff,chapter=chapter)
            
            questions.append(q)
    
    #print(len(questions))       
    
    return questions
