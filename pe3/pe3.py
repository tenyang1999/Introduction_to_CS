# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:42:38 2023

@author: tenyang
"""

print('Welcome to the simple Rock-Paper-Scissors Game!')

player1 = input("Enter Player 1's name：")
player2 = input("Enter Player 2's name：")

p1_score = 0
p2_score = 0

play = True

while play:
    p1_choice = input("%s , enter your choice (rock,paper, or scissors):" %(player1))
    p2_choice = input("%s , enter your choice (rock,paper, or scissors):" %(player2))
    
    if p1_choice == 'rock':
        if p2_choice == 'rock':
            print("It's a tie!")
        elif p2_choice == 'paper':
            print("%s wins this round!" %(player2))
            p2_score += 1
        else:
            print("%s wins this round!" %(player1))
            p1_score += 1
    elif p1_choice == 'paper':
        if p2_choice == 'rock':
            print("%s wins this round!" %(player1))
            p1_score += 1
                   
        elif p2_choice == 'paper':
            print("It's a tie!")       
        else:
            print("%s wins this round!" %(player2))
            p2_score += 1
    else:
        if p2_choice == 'rock':
            print("%s wins this round!" %(player2))
            p2_score += 1
        elif p2_choice == 'paper':
            print("%s wins this round!" %(player1))
            p1_score += 1
        else:
            print("It's a tie!")     
            
    
    ask = input("Do you want to continue the game? (yes or no):")
    if ask == "no":
        play = False    
        print("%s's socre:%d" %(player1,p1_score))
        print("%s's socre:%d" %(player2,p2_score))
        if p1_score > p2_score:
            print("%s is the final winner!" %(player1))
        elif p1_score == p2_score:
            print("It's a tie!")
        else:   
            print("%s is the final winner!" %(player2))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    