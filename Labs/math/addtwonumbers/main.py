"""
Math and Variables Lab
By: Janet Griffin
CSCI 110 Lab
Date: 02/06/2024
Due Date: 02/15/2024 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main():
    """Main function that solves the problem
    """

    # FIXME1 - read input data into a variable #fixed#
    line = input()

    # split the data into two numbers
    a, b = line.split()

    # check to see if the data is split correctly
    print(f'{a=}, {b=}', file=sys.stderr)

    # FIXED2: convert string a into integer #fixed#
    a = int(a)

    # FIXED3: convert string b into integer #fixed#
    b = int(b)

    # FIXED4: add two numbers and store the result into ans variable #fixed#
    sum = a + b 

    # FIXED 5: print the answer as shown in the sample output #fixed#
    print(sum)


# call main function
main()  
    
