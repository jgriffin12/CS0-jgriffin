'''
Name: Janet Griffin
Date: 04/03/2024
Program: Kattis Problem - Simon Says https://open.kattis.com/problems/simonsays
Description: For each input that begins with, "Simon says", the program should listen to what the input says. If the input does not begin with,
 "Simon says", ignore the instruction. 
'''

# Function that determines if input starts with "Simon says..." - Will read each element in dictionary.
def simonSays(simonCommand):
    # Checks to see if simonCommand input starts with "Simon says "
    if simonCommand.startswith("Simon says "):
        return simonCommand[len("Simon says "):]
    else:
        return None

# Test functions for answer
def test_answer():
    ans = simonSays("Simon says raise right hand")
    expected = "raise right hand"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer2():
    ans = simonSays("raise right hand")
    expected = None 
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer3():
    ans = simonSays("Simon says laugh.")
    expected = "laugh."
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# Main function
def main():
    # Number of commands
    numCommands = int(input())

    # For loop - reads input number of numCommands
    for _ in range(numCommands):
        simonCommand = input()

        answer = simonSays(simonCommand)
        if answer != None:
            print(answer)

if __name__ == "__main__":
    main()
    test_answer()
    test_answer2()
    test_answer3()

    