# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:00:44 2023

@author: tenyang
"""

num = int(input("Enter a positive integer:"))
an_list = []
for i in range(num):  # 判斷由1-num間的數值
  list_i = list(str(i)) # 將數值轉換成一個一個的字元
  num_len = len(list_i) # 判斷總共有幾次方
  count = 0
  for j in list_i: # 取出每一個字元乘幾次方
    count += int(j)**num_len
  
  if count == i:
    an_list.append(i)

print("Armstrong Number from 1 to %s are :"%(num), an_list)