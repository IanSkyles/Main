"""
Ian Skyles
March 17th, 2015
An Introduction to Interactive Programming in Python (Part 1)
Mini Project #1 Rock, paper, scissors, lizard, spock
"""

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#import statements
import random

# helper functions

def name_to_number(name):
    # Converts a item name (ie rock, lizzard) to a integer representatio

    # convert name to number using if/elif/else
    if (name == "rock"):
        numberRepresentation = 0        
    elif (name == "Spock"):
        numberRepresentation = 1
    elif (name == "paper"):
        numberRepresentation = 2
    elif (name == "lizard"):
        numberRepresentation = 3
    elif (name == "scissors"):
        numberRepresentation = 4
    else:
        print "error in name_to_number"
    # don't forget to return the result!
    return numberRepresentation


def number_to_name(number):
    # Converts a number to a name
    
    # convert number to a name using if/elif/else
    if (number == 0):
        nameRepresentation = "rock"       
    elif (number == 1):
        nameRepresentation = "Spock"
    elif (number == 2):
        nameRepresentation = "paper"
    elif (number == 3):
        nameRepresentation = "lizard"
    elif (number == 4):
        nameRepresentation = "scissors"
    else:
        print "error in number_to_name"
    # don't forget to return the result!
    return nameRepresentation
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if(difference == 0):
        print "Player and computer tie!"
    elif(difference < 3):
        print "Computer wins!"    
    elif(difference < 5):
        print "Player wins!"
    else:
        print "Error in rpsls"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


