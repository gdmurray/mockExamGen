"""
-------------------------------------------------------
Question_Class.py
Creates an object of a question to manipulate
-------------------------------------------------------
Author:  Gregory Murray
ID:      #########
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-02"
-------------------------------------------------------
"""
class Question():
    
    _question_list = []
    
    def __init__(self, question_text, options, answer, difficulty, chapter):
        self.question_text = question_text
        self.options = options
        self.answer = answer
        self.difficulty = difficulty
        self.chapter = chapter
        
        return
    
    def __str__(self):
        return str("""
{}
{}
{}
{}
Chapter:{}
        """.format(self.question_text, self.options, self.answer, self.difficulty,self.chapter))
    
    def _append(self,_question_list):
        return _question_list.append(self)
        