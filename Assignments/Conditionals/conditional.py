'''
Name: Janet Griffin 
Date: 3/6/2024
Program: Conditional Python Calculator
Description: This program will compute the sum, product, max, min, and average of any 5 given numbers. 
'''

# Function called sum that takes 5 numbers and returns the sum.
def sum(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    return sum 

# Function called product that takes 5 numbers and returns the product of them.
def product(num1, num2, num3, num4, num5):
    product = num1 * num2 * num3 * num4 * num5
    return product

# Function called average that uses the sum function to calculate average of 5 numbers. 
def average(num1, num2, num3, num4, num5):
    average = sum(num1, num2, num3, num4, num5) / 5
    print("Average of (", num1, "+" ,num2, "+", num3, "+", num4, "+", num5, ") / 5 =", average)

# Function called largestNumber that takes 5 numbers and finds the largest value. 
def largestNumber(num1, num2, num3, num4, num5):
    if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
        print("The largest number is", num1)
    elif(num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
        print("The largest number is", num2)
    elif(num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
        print("The larget number is", num3)
    elif(num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
        print("The largest number is", num4)
    else:
        print("The largest number is", num5)

# Function called smallestNumber that takes 5 numbers and finds the smallest value. 
def smallestNumber(num1, num2, num3, num4, num5):
    if (num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5):
        print("The smallest number is", num1)
    elif(num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5):
        print("The smallest number is", num2)
    elif(num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5):
        print("The smallest number is", num3)
    elif(num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5):
        print("The smallest number is", num4)
    else:
        print("The smallest number is", num5)

# Test functions
def test(num1, num2, num3, num4, num5):
    assert (sum(1, 2, 3, 4, 5) == 15.0)
    assert (sum(5, 5, 5, 5, 5) == 25.0)
    assert (product(2,2,2,2,2) == 32.0)
    assert (product(10,0,5,8,7) == 0.0)
    assert (average(10,4,3,2,1) == 4.0) 
    assert (average(100,20,10,5,5) == 28.0)
    assert (largestNumber(1000,5,-1,3,4) == 1000.0)
    assert (largestNumber(4,3,11,20,80) == 80.0)
    assert (smallestNumber(0,1,2,3,4,5) == 0.0)
    assert (smallestNumber(0.5,6,9,3,1) == 0.5)
    print("All test cases passed...")

# Main function
def main():

    # Print function that is welcoming the user. Prompts user to input 5 numbers.
    print("Welcome to my Conditional Python Calculator! Please enter 5 numbers: \n")

    # Stores user input into the following variables.
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    num3 = float(input("Number 3: "))
    num4 = float(input("Number 4: "))
    num5 = float(input("Number 5: "))

    # Call sum function
    print("\nSum of", num1, "+" ,num2, "+", num3, "+", num4, "+", num5, "=", sum(num1, num2, num3, num4, num5))

    # Call product function5
    print("Product of", num1, "*" ,num2, "*", num3, "*", num4, "*", num5, "=", product(num1, num2, num3, num4, num5))

    # Call average function
    average(num1, num2, num3, num4, num5)

    # Call largestNumber function
    largestNumber(num1, num2, num3, num4, num5)

    # Call smallestNumber function
    smallestNumber(num1, num2, num3, num4, num5)

    # Call test function 
    test(num1, num2, num3, num4, num5)

main()

