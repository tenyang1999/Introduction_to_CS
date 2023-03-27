# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:40:54 2023

@author: tenyang
"""

amt = int(input("Enter the shopping amount："))
mem_level = input("Enter the member level(Regular or Gold)：")

if mem_level =="Gold":
  if amt >= 3000 :
    discount_amt = amt*0.75
    print(mem_level,"$",str(discount_amt))
  elif amt >= 2000 :
    discount_amt = amt*0.8
    print(mem_level,"$",str(discount_amt))
  elif amt >= 1000:
    discount_amt = amt*0.85
    print(mem_level,"$",str(discount_amt))
  else:
    discount_amt = amt
    print(mem_level,"$",str(discount_amt))
elif  mem_level =="Regular":   
  if amt >= 3000 :
    discount_amt = amt*0.8
    print(mem_level,"$",str(discount_amt))
  elif amt >= 2000 :
    discount_amt = amt*0.85
    print(mem_level,"$",str(discount_amt))
  elif amt >= 1000:
    discount_amt = amt*0.9
    print(mem_level,"$",str(discount_amt))
  else:
    discount_amt = amt
    print(mem_level,"$",str(discount_amt))
else:
  print("Invalid member level.Please enter 'Regular or Gold'")