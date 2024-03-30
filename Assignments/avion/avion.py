"""
Name: Janet Griffin
Date: 3/27/2024
Program: Kattis Problem - Avion https://open.kattis.com/problems/avion
Description: 
CIA blimps have "FBI" somewhere in registration codes. This program will point out all CIA blimps given 5 rows of input. A 
registration code will be a max of 11 uppercase letters, digits 0-9, or dashes (-):
If CIA blimps are found, ouput will list row number. 
If no CIA blimps are found, program will print, "HE GOT AWAY!"
"""

# Function called getData that receives input
def getData():
    data = input()
    return data 

# Function to find CIA blimps. 
def findAgent():
    # Empty list called ciaBlimp to store row numbers if string contains 'FBI'.
    ciaBlimp = []
    string_list = []
    count = 1
    # Loop 5 times (receive 5 rows of input) and calls getData function to receive and store input into string_list
    for _ in range (5):
        string_list.append(getData())
    # For each element in string_list, if 'FBI' is found, count # is added to ciaBlimp list and count # increments by one. Otherwise, only increment count # by one. 
    for i in string_list:
        if 'FBI' in i:
            ciaBlimp.append(count)
            count += 1
        else:
            count += 1
            continue
    # If ciaBlimp list is empty, there is no 'FBI' strings caught by program. Print "HE GOT AWAY!"
    if len(ciaBlimp) == 0:
        zeroAgent = print("HE GOT AWAY!")
        return zeroAgent
    else:
        #Removing brackets and commas from list ciaBlimp.
        final_agentcount = print(*ciaBlimp, sep= " ")
        return final_agentcount

# Main function
def main():
   
    findAgent()
    
main()

