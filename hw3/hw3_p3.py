# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:44:10 2023

@author: tenyang
"""

def judge_winner(B):
    
    
    ans_list = []
    lines = [4,5,6,7] # 表示幾個組成一條線 
    
    for l in lines:
        horizontal  = [1]*l 
        k = l
        for i in range(6): #由上往下
            for j in range(7-k+1): #由左往右
                tar = B[i][j:j+k]
                cnt = 0
                for num in range(k):
                    cnt += horizontal[num]*tar[num]
                if cnt == l:
                    return("Winner X")
                elif cnt == -l:
                    return("Winner O")               
    for l in lines:
        vertical  = [1]*l 
        k = l
        for j in range(7):#由左往右
            for i in range(6-k+1):#由上往下
                cnt = 0
                for num in range(k):
                    cnt += vertical[num]*B[i+num][j]
                if cnt == l:
                    return("Winner X")
                elif cnt == -l:
                    return("Winner O")
                    
    for l in lines:
        neg_cross  = [1]*l 
        k = l
        for i in range(6-k+1): #由上往下
            for j in range(7-k+1-1,7): #由左往右
                cnt = 0
                for num in range(k): #往左下取
                   cnt += neg_cross[num]*B[i+num][j-num]
                if cnt == l:
                    return("Winner X")
                elif cnt == -l:
                    return("Winner O")
    for l in lines:
        
        pos_cross  = [1]*l 
        k = l
        for i in range(6-k+1): #由上往下
            for j in range(7-k+1): #由左往右
                cnt = 0
                for num in range(k): #往左下取
                   cnt += pos_cross[num]*B[i+num][j+num]
                if cnt == l:
                    return("Winner X")
                elif cnt == -l:
                    return("Winner O")

horizontal = "+---"*7+"+"
vertical = "|"


for i in range(6):
    print(horizontal)
    print((vertical+"   ")*7+vertical)
print(horizontal)
print('  '+'0'+'   '+'1'+'   '+'2'+'   '+'3'+'   '+'4'+'   '+'5'+'   '+'6')

correct = [0,1,2,3,4,5,6]
cnt = 0

A=[[0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],]

B =[[0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0],] 


player = 1

while cnt< 42:
    # playerX = 1 , playerO = 0
    if player == 1:
        play = input("Player X >> ")
    else :
        play = input("Player O >> ")
    
    if play.isnumeric():
        if int(play) not in correct:
            print("Out of range, try again [0‐6].")
            continue
    else:   
        print("Invalid input,  try again [0‐6].")
        continue
    
    col = int(play)
    row = 5
    while row >= -1 :
        if A[row][col] == "X" or A[row][col] =='O':
            row -= 1
        else:
            if player == 1:
                A[row][col] = "X"
                B[row][col] = 1
            else:
                A[row][col] = "O"
                B[row][col] = -1
            break
        if row == -1:
            print("This column is full. Try another column")
        
    
    for i in range(6):
        print(horizontal)
        for j in range(7):
            if A[i][j] == 0 :
                blank = "   "
            else:
                blank = " "+A[i][j]+" "
            print(vertical+blank,end="")
        print(vertical)   
    print(horizontal)
    print('  '+'0'+'   '+'1'+'   '+'2'+'   '+'3'+'   '+'4'+'   '+'5'+'   '+'6')
    
    ans = judge_winner(B)
    if ans != None:
        print(ans)
        break

    if player == 1:
        player -=1
    else :
        player +=1
    cnt += 1
    
    if cnt >= 42:
        print("ALL column are full,the game ends in a draw")
        break
    
    
    
    
    
    