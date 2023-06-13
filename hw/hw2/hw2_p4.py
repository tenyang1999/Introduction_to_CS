# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:54:30 2023

@author: tenyang
"""

layer = int(input("Enter the number of layers (2 to 5):"))
top_len = int(input("Enter the side length of the top layer:"))
growth = int(input("Enter the growth of each layer:"))
trunk_w = int(input("Enter the trunk width(odd number, 3 to 9):"))
trunk_h = int(input("Enter the trunk heigth(4 to 10):"))

# 最頂層為top_len-2個點，layer1為2@，再逐層增加growth，再加一
space = 2 + (layer-1)*growth + 1
height = top_len-2

i =1
while i <= layer:
    # top層
    if i == 1:
        print(' '*(space)+'#')
        
    # 內核層
    j = 1
    while j <= (height):
        at_ = 1+2*(j-1)
        print(' '*(space-j)+'#'+"@"*at_+"#")
        j +=1
    
    # 底層
    bottom = 1+2*(j-1)+2
    print(' '*(space-height-1)+'#'*bottom)
    
    height += growth
    i = i+1

k = 1
while k <= trunk_h:
    trunk_s = space-(trunk_w//2)
    print(" "*trunk_s + "|"*trunk_w)
    k+=1
    
    
    
    
    
