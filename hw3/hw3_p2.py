# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:01:19 2023

@author: tenyang
"""

poly = "-X^3-12*X^2+100 "  # input("Input polynomial:")
X = 3 #inpuy('Input the value of X:')
li =[]

# 第一階段：先將整個字串拆解成數字跟運算符
num = None
for i in poly:
    
    if i.isnumeric():
        if num == None:
            num = i
        else:
            num = num+i
    elif num != None:
        li.append(int(num))
        num = None
        
    if i =="X":
        li.append(X)
    elif i == "^":
        li.append("**")
    elif i == "*":
        li.append("*")
    elif i == '-':
        li.append(-1)
        li.append("*")
if  num != None:
    li.append(int(num))

j = 0
while j < len(li):
    if li[j] =="**":
        li[j-1] = li[j-1]**li[j+1]
        del li[j]   
        del li[j]
        j = 0
    j +=1
j = 0
while j < len(li):
    if li[j] =="*":
        li[j-1] = li[j-1]*li[j+1]
        del li[j]   
        del li[j]
        j = 0
    j +=1        
    
print("Evaluated Result:",sum(li))

"""
Method 2
while "*" in li :
    while "**" in li:
        j = li.index('**')
        li[j-1] = li[j-1]**li[j+1]
        del li[j]   
        del li[j]
        print(li)
    j = li.index('*')
    li[j-1] = li[j-1]*li[j+1]
    del li[j]   
    del li[j]  
    
print("Evaluated Result:",sum(li))
"""
        