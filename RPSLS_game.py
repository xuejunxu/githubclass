"""
Design a small project to play the Rock-paper-scissors-lizard-Spock game
"""

def name_as_number(name):
	"""
	Build a helper function name_to_number(name) that converts the string name into a number between 0 and 4
	"""
	if name=='rock':
		return 0
	elif name=='Spock':
		return 1
	elif name=='paper':
		return 2
	elif name=='lizard':
		return 3
	elif name=='scissors':
		return 4
	else:
		print("Error: Invalid Input!")

def number_as_name(number):
	"""
	Build a helper function number_as_name(number) that converts the number between range 0 to 4 into string name
	"""
	if number==0:
		return 'rock'
	elif number==1:
		return 'Spock'
	elif number==2:
		return 'paper'
	elif number==3:
		return 'lizard'
	elif number==4:
		return 'scissors'
	else:
		print("Error: Invalid number! Please input number from 0 to 4!")

import random
def rpsls(player_choice):
	"""
	Buliding the main part of the game. Getting the input from user and comparing the result with the computer's random choice, and deciding who wins.
	Print out the results.
	"""
	player_number=name_as_number(player_choice)
	print("Player chooses "+player_choice)
	comp_number=random.randint(0,4)
	comp_choice=number_as_name(comp_number)
	print("Computer chooses "+comp_choice)
	diff_comp_player=(comp_number-player_number)%5
	if diff_comp_player==0:
		print("Player and computer tie!")
	elif (diff_comp_player==1) or (diff_comp_player==2):
		print("Computer wins!")
	else:
		print("Player wins!")
	print("")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
