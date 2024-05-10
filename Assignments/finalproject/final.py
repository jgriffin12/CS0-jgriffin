'''
Name: Janet Griffin
Date: 05/03/2024
Program: Harry Potter Hangman Game
Description: The program selects a random word from our Harry Potter Dictionary. As the player, you must take turns guessing a letter from the random word. If that guess is correct, 
nothing happens and you can guess again. If the guess is incorrect, the wizard gets one step closer to being hanged. You have 6 wrong guesses before the wizard dies.

'''
import random
import sys

# Function reads words.txt file and appends to list called hp_list. Returns list
def readFile():
    # Create empty list to store words from words.txt file
    hp_list = []
    # Opening file in read mode
    file = open('words.txt', 'r')
    words = file.readlines()
    # Removes the '\n\ from list and appends modified elements to hp_list.
    for line in words:
        if line[-1] == '\n':
            hp_list.append(line[:-1])
    return hp_list # ['this','is','the','format']

# Function to pick random word from list - returns random word from list and makes sure all letters are same format - uncapitalized
def rand_word(list):
    word = random.choice(list) # word
    lower_word = word.lower()
    return lower_word

# Function prompts user to take guess
def take_guess():
    print("\nGuess a letter: ")
    guess = str(input())
    return guess
    
# Function checks user guess to see if letter is in word - returns True or False 
def check_letter(guess, game_word):
    if (guess in game_word):
        print("\nYou got a letter!")
        return True
    else:
        print("\nSorry, that is not in the magic word.Try again!")
        return False

# Function displays guessed letters _ _ a _ _
def display_letters(correct_guess, game_word):
    display = ""
    for letter in game_word:
        if letter in correct_guess:
            display += letter
        elif (letter == " "):
            display += " "
        else:
            display += "_ "
    return display

# Function to ask if player wants to keep playing
def keep_playing():
    ans = str(input("Would you like to play again? Enter [Y|y] if you want to continue. "))
    if (ans == 'y'):
        return True
    else:
        return False

def image(count):
    # No wrong answers
    if (count == 0):
        image = """ 
                             __________
                            |          |
                            |     
                            |     
                            |
                            |
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    # 1 wrong answer
    elif (count == 1):
        image = """ 
                             __________
                            |        |
                            |     __/=\__    
                            |      
                            |
                            |
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    # 2 wrong answers
    elif (count == 2):
        image = """ 
                             __________
                            |        |
                            |     __/=\__    
                            |      (o o)
                            |
                            |
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    # 3 wrong answers
    elif (count == 3):
        image = """ 
                            __________
                            |        |
                            |        |
                            |     __/=\__    
                            |      (o_o)
                            |      /   \ 
                            |     |_____|
                            |    
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    # 4 wrong answers
    elif (count == 4):
        image = """ 
                            __________
                            |        |
                            |        |
                            |     __/=\__    
                            |      (o_o)
                            |    \ /   \ / 
                            |     |_____|
                            |     
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    # 5 wrong answers 
    elif (count == 5):
        image = """ 
                            __________
                            |        |
                            |        |
                            |     __/=\__    
                            |      (o_o)
                            |    \ /   \ /
                            |     |_____|
                            |      _| |_
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)
    else:
        image = """ 
                            __________
                            |        |
                            |        |
                            |     __/=\__   | 
                            |      (o_o)    |
                            |    \ /   \ / _|_
                            |     |_____|  |||
                            |      _| |_  ||||| 
                            |
                        MMMMMMMMMMMMMMMMMMMM
                """
        print(image)        

# Main function
def main():

    while (True):  
          
        # Calls function to read txt file into list.
        list = readFile()

        # Program chooses random word from list.
        game_word = rand_word(list)

        # Introduce player to game
        print("Welcome to Harry Potter Hangman!\n")
        print("Rules of Game: \n")
        print("The program selects a random word from our Harry Potter Dictionary. As the player, you must take turns guessing a letter from the random word.")
        print("If that guess is correct, nothing happens and you can guess again. If the guess is incorrect, the wizard gets one step closer to being hanged.")
        print("You have 6 wrong guesses before the wizard dies. \n")

        # While loop - loops if error != 7
        count = 0
        correct_guess = []
        guesses_made = []
        list = []
        while (count < 6):
            guess = take_guess()
            # Calls to check if guess is in game_word
            if (check_letter(guess,game_word) == True):
                
                image(count)
                correct_guess.append(guess)
            else:                                                         
                count += 1
                guesses_made += guess
                image(count)

            word = display_letters(correct_guess, game_word)
            print("Incorrect Guesses Made: ", *guesses_made)

            # If game word is guessed before 6 wrong guesses - player wins
            if (word == game_word):
                print("Huzzah!", "The word was", game_word, ". You won Harry Potter Hangwizard! \n")
                break
            else:
                print(word)
        if (count == 6):
            # If player gets to this point, they lose
            print("Avada Kedavra!! You did not guess the magic word within 6 tries. The wizard has died.")
            print("The magic word was", game_word, "\n")

        # Check and see if player wants to continue playing
        if (keep_playing() == True):
            continue
        else:
            sys.exit()


main()