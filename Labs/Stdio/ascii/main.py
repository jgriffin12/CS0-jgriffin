"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Janet Griffin #FIXED1
    Date: 1/31/2024 #FIXED2
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

# FIXME3: prompt user to enter their name and store the value into name variable using input function

name: str = input("What is your name? ")

# FIXME4: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!

print("Nice to meet you, " + name + "!\n")


# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

# FIXME5: prompt user to enter the year and store the value into year variable using input function

year_input: str = input("What is the year? ")

# FIXME6: print the year using the variable as the following output
# must output: This is <year> year.

print("This is " + year_input + "." )

print("Hope you like my ASCII art...\n\n")

line1: str = "   |\\_/|       *****************************    (\\_/)"
print(line1)

# FIXME7: use variable to print the second line of the graphic

secondLine: str = "  / @ @ \      *        ASCII Lab          *   (='.'=)"
print(secondLine)

# FIXME8: print the third line of the graphics

thirdLine: str = ' ( > 0 < )     *      Janet Griffin        * ( " )_( " )'
print(thirdLine)


# FIXME9: use variable to print the fourth line

fourthLine: str = "   >>x<<       *       Spring 2024         *"
print(fourthLine)

# FIXME10: use variable to print the fifth line

fifthLine: str = "  /  O  \      *        CSCI 110           *"
print(fifthLine)

# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

sixthLine: str = "               *****************************  "
print(sixthLine)

print("\nGood bye...  \n")
