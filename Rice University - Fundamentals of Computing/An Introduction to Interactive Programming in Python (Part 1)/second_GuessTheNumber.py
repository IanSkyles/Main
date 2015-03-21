# Ian Skyles
# Mini Project 2: Guess the number
# March 17th, 2015 (3/17/2015)

# input will come from buttons and an input field
# all output for the game will be printed in the console

#imports
import simplegui
import random

secret_number = 0
number_of_guesses = 7
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables
    global secret_number
    global num_range
    global number_of_guesses
    # assign secret number based on number range, default range is 0-99
    secret_number = random.randrange(0, num_range)
    
    if(num_range == 100):      
        number_of_guesses = 7
    elif(num_range == 1000):      
        number_of_guesses = 10
    print "New game. Range is from 0 to " + str(num_range)    
    print "Number of remaining guesses is " + str(number_of_guesses)
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    
    
def input_guess(guess):
    # main game logic here
    global number_of_guesses
    global num_range
    global secret_number
    #code assumes variable is an integer, haven't learned how to check if it is yet
    guess_to_number = int(guess)
    print
    print "Guess was " + guess
    number_of_guesses = number_of_guesses - 1    
    if(number_of_guesses == 0):
        print "You ran out of guesses. The number was " + str(secret_number)
        print
        new_game()
    else:       
        
        if(guess_to_number == secret_number):
            print "You guessed the secret number!"
            print
            new_game()
        else:
            print "Number of remaining guesses is " + str(number_of_guesses)
            if(guess_to_number > secret_number):
                print "Guess lower!"
            elif(guess_to_number < secret_number):
                print "Guess higher!"
            else:
                print "Error in input_guess"   
    
    
def button_handler_range_100():
    #start a new game with secret number in range 0-99    
    #handles button clicked events
    range100()
    print
    new_game()

def button_handler_range_1000():
    #start a new game with secret number in range 0-999
    #handles button clicked events
    range1000()
    print
    new_game()


    
# create frame
frame = simplegui.create_frame("Guess a number", 200, 200)
#add input listener
inp = frame.add_input("My Number", input_guess, 100)
#add buttons
button1 = frame.add_button('Range 100', button_handler_range_100)
button2 = frame.add_button('Range 1000', button_handler_range_1000)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()

