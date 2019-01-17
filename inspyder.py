# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:21:59 2019

@author: User
"""

import IPython
from IPython.display import clear_output

def display_board(board):
    
    clear_output() 
    
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_input():
    marker=''
    while marker!='X'and marker!='O':
        marker=input('Player1: Choose X or O: ').upper()
        
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
    
player1_marker, player2_marker= player_input()


def input_position():
    print("Please enter the position")
    position=input()
    return position

def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark)or(board[4]==mark and board[5]==mark and board[6]==mark)or(board[1]==mark and board[2]==mark and board[3]==mark)or(board[1]==mark and board[4]==mark and board[7]==mark)or(board[2]==mark and board[5]==mark and board[8]==mark)or(board[3]==mark and board[6]==mark and board[9]==mark)or(board[1]==mark and board[5]==mark and board[9]==mark)or(board[3]==mark and board[5]==mark and board[7]==mark))
               
import random
from random import randint

def choose_first():
    y=randint(0,1)
    if y==1:
        print("Player 1 goes first")
        return 1
    else:
        print("Player 2 goes first")
        return 0
    
def space_check(board,position):
    return board[position]==" "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose your position: (1-9) '))
        
    return position

def repeat():
     print("Do you wanna play again? Enter yes or no")
     a=input()
     if a=="yes":
         user_repeat=True
     else:
         user_repeat=False
     return user_repeat
                    
                    
user_repeat=True
while user_repeat==True:
      
    print("WELCOME TO TIC TAC TOE")
        
    print("Do you wanna play? Enter yes or no.")
    a=input().lower()
    if a=="yes":
        print("Let's Play")
        z=True
    else:
        z=False
    
    myboard=[" "]*10
    player1_marker, player2_marker= player_input()
    going_first=choose_first()
    while z==True:
        
        display_board(myboard)
        while going_first==1 and z==True:
            print("Player 1 chance")
            position=player_choice(myboard)
            place_marker(myboard,player1_marker,position)
            display_board(myboard)
            
            if win_check(myboard,player1_marker):
                display_board(myboard)
                print("Player 1 has won")
                z=False
                repeat()
               
                
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("Match is draw!")
                    z=False
                    repeat()
                else:
                    print("Chance of Player 2")
                    going_first=0
    
           
                
        while going_first==0 and z==True:
            print("Player 2 chance")
            position=player_choice(myboard)
            place_marker(myboard,player2_marker,position)
            display_board(myboard)
            
            if win_check(myboard,player2_marker):
                print("Player 2 has won")
                z=False
                repeat()
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("Match is draw!")
                    z=False
                    repeat()
                else:
                    print("Chance of Player 1")
                    going_first=1
    





        