'''
Name: Janet Griffin
Date: 03/11/2024\
Program: Guess the Number Game
Description: This program will welcome user and ask the user to guess a number between 1-20. The program will loop until game is over:
    Player must guess the correct number within 6 tries (Winner).
    Player doesn't guess correctly within 6 tries (Loser).
    Program must notify player if the guess is too low or too high. 
'''
import random 

# Function that welcomes user to game.
def welcome():
    print("Welcome to --Guess the Number-- game! \nWhat is your name?")

# Function that gets users name and notifies user of prompt.
def getName():
    name = str(input())
    print(f"Hello, {name}. I am thinking of a number between 1 and 20.")

# Function to get user to guess numbers
def guessNum():
    # Program chooses random number between 1 and 20 (non-inclusive) - set random seed
    programNum = random.randint(2,19)
    # Set total to 0
    total = 0
    # Initialize number of tries to 1.
    tries = 1
    # Loop will allow 6 guesses by user
    for i in range(0,6):
        # Guess by user
        userGuess = int(input("Take a guess between 1-20 (non-inclusive):"))
        # Making sure guess number is within correct range.
        if (userGuess > 1 and userGuess < 20):
            # Compare userGuess num to the random generated program number.
            if (userGuess > programNum):
                # Add number of tries to total
                total += tries 
                print("Your guess is too high.")
            elif (userGuess < programNum):
                total += tries 
                print("Your guess is too low.")
            else:
                total += tries
                print("Congratulations. You win!!")
                print("You guessed my number in", total, "tries.")

        else:
            print ("Guess is invalid. Please enter a number between 1 and 20.")
    # If number not guessed during loop, user does not win guessing game.
    if (userGuess != programNum):
        print("Oh no! You lose. You did not guess the correct number within 6 tries.")
        print("The secret number is", programNum)

# Main Function
def main():

    welcome()
    getName()
    guessNum()

main()