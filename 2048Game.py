"""
This program presents the Game 2048
"""

import curses
import random
import collections

#define user actions. 
#w for up, a for left, s for down, d for right
#q for quit, r for restart
user_actions=['up','left','down','right','quit','restart']

#return the unicode of the input characters
letter_uni_code=[ord(char) for char in 'WASDQRwasdqr']
#pairing input characters with user actions
paired_letter=zip(letter_uni_code,user_actions*2)
#