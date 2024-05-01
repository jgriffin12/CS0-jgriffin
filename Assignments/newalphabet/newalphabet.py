'''
Name: Janet Griffin
Date: 04/24/2024
Program: Program translates phrase from the old dictionary to the new. 
Description: The program will read a string input by user. It will then translate that string using the new alphabet.

'''
# Function that uses string[] and translates string[] letters to the new characters in newalpha
def translate(string):
    newalpha = {'a' : "@", 'b' : "8", 'c':"(", 'd':"|)", 'e':"3", 'f':"#", 'g':"6", 'h':"[-]", 'i':"|", 'j':"_|", 'k':"|<", 'l':"1",
    'm':"[]\/[]", 'n':"[]\[]", 'o':"0", 'p':"|D", 'q':"(,)", 'r':"|Z", 's':"$", 't':"']['", 'u':"|_|", 'v':"\/", 'w':"\/\/", 'x':"}{",'y':"`/",
    'z':"2"} 
    # List that contains translated letteres 
    translated_alpha = []
    for ch in string:
        if ch.lower() in newalpha:
            if ch.isupper():
                translated_alpha += newalpha[ch.lower()].upper()
            else:
                translated_alpha += newalpha[ch]
        else:
            translated_alpha += ch
    return translated_alpha

# Function that splits user string into individual letters and saves in string list[]
def split_string(user_string):
    string = []
    for letter in user_string:
        string.append(letter)
    return string # returns ['H','e','l','l','o']

# Function to test if user string is split. 
def test_split_string():
    userinput = "Hello"
    ans = split_string(userinput)
    assert (ans == ['H','e','l','l','o'])

# Test translate() with lowercase
def test_translate1():
    string = ['h','e','l','l','o']
    ans = translate(string)
    assert (ans == ['[', '-', ']', '3', '1', '1', '0'])

# Test translate() with uppercase
def test_translate2():
    string = ['H','E','L','L','O']
    ans = translate(string)
    assert (ans == ['[', '-', ']', '3', '1', '1', '0'])

# Test translate() with mixed upper and lower 
def test_translate3():
    string = ['H','e','L','l','O']
    ans = translate(string)
    assert (ans == ['[', '-', ']', '3', '1', '1', '0'])

# Main function 
def main():

    # Reads string input from user.
    user_string = str(input())
    # passes user_string into split_string()
    string = split_string(user_string)
    # call function translate
    print("".join(translate(string)))
   
if __name__ == "__main__":
    test_translate1()
    test_translate2()
    test_translate3()
    main()