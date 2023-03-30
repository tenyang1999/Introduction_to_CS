# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:38:38 2023

@author: tenyang
"""

num = int(input("Input the total number of students(n>0):"))

stud = [i for i in range(1,num+1)]

cnt = 1

# stud index in list
j = 0
while len(stud) > 1:    
    
    if cnt == 3:
        # 因為del後，後面的index會往前1，所以不用+1
        del stud[j]
        cnt = 0
    else:
        j+=1
        
    cnt += 1
    
    # 當index長度大於list長度就從頭開始
    if j >= len(stud) :
        j = 0

print(stud[0])
