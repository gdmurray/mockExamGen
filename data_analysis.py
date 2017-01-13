"""
-------------------------------------------------------
data_analysis.py
prints basic statistics of the exam test bank
-------------------------------------------------------
Author:  Gregory Murray
ID:      150236640
Email:   murr6640@mylaurier.ca
__updated__ = "2016-04-03"
-------------------------------------------------------
"""
import Main

questions = Main.create_questions()

count = 0
A_Count = 0
B_Count = 0
C_Count = 0
D_Count = 0
E_Count = 0

for q in questions:
    if q.answer == 'A':
        A_Count += 1
    elif q.answer == 'B':
        B_Count+=1
    elif q.answer == 'C':
        C_Count +=1
    elif q.answer == 'D':
        D_Count +=1
    elif q.answer == 'E':
        E_Count +=1
    count +=1

print('Percentages:')
print("A's: {:.0f}%".format((A_Count / count) * 100))
print("B's: {:.0f}%".format((B_Count / count) * 100))
print("C's: {:.0f}%".format((C_Count / count) * 100))
print("D's: {:.0f}%".format((D_Count / count) * 100))
print("E's: {:.0f}%".format((E_Count / count) * 100))


        