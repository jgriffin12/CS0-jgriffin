'''
Name: Janet Griffin
Date: 02/19/2024
Program: My Calculator Program
Description: Functions - Create a Python program that performms arithmetic operations given two numbers (by user).
'''
import math

# Function named add_two that sums two numbers (number1, number2)
def add_two(number1, number2):
    sum = number1 + number2
    print(f"The sum of {number1} and {number2} = {sum}")

# Function named multiply_two that returns product of two numbers (number1, number2)
def multiply_two(number1, number2):
    product = number1 * number2
    print(f"The product of {number1} * {number2} = {product}")

# Function named divide_two that divides number1 by number2 and returns quotient.
def divide_two(number1, number2):
    quotient = number1 / number2
    print(f"The quotient of {number1} / {number2} = {quotient}")

# Function named subtract_two that subtracts number2 from number1 and returns the difference.
def subtract_two(number1, number2):
    difference = number2 - number1
    print(f"The difference of {number2} - {number1} = {difference}")

# Function named remainder that returns remainder of two numbers. - Make sure this is working correctly.
def remainder(number1, number2):
    modulo = number1 % number2
    print(f"The remainder of {number1} / {number2} = {modulo}")
    
# Funtion named power that takes number1 to the nth(number2) power and returns the value.
def power(number1, number2):
    nthpower = number1 ** number2
    print(f"{number1} to the {number2}th power = {nthpower}")

# Function named root that takes the square root of number1 
def root(number1):
    squareRoot1 = math.sqrt(number1)
    print(f"The square root of {number1} = {squareRoot1}")


def test():
    # 5+6 = 11 == True
    # -5+10 = 5
    assert 11, add_two(5,6) == True
    assert 5, add_two(-5,10) == True
    # -3 * 10 = 30 == True
    # 5 * 2 = 10 == True
    assert -30, multiply_two(-3,10) == True
    assert 10, multiply_two(5,2) == True
    # 10 / 4 = 2.5 == True 
    # 20 / 4 = 5 == True
    assert 2.5, divide_two(10,4) == True
    assert 10, divide_two(20,5) == True
    # number2(25) - number1(50) = -25 --- (number1,number2)
    # 100 - 30 = 70 == False
    assert -25, subtract_two(50,25) == True
    assert 70, subtract_two(30,100) == True
    # 10%2 = 0 == True
    # 10%3 = 1 == True
    assert 2, remainder(10,4) == True
    assert 1, remainder(10,3) == True
    # 4^8 = 65536 == True 
    # 6^2 = 36 == True
    assert 65536, power(4,8) == True
    assert 36, power(6,2) == True 
    # sqrt(4) = 2
    # sqrt(9) = 3
    assert 2, root(4) == True
    assert 3, root(9) == True 
    print("All test cases passed.\n")
    

def bonus(number1, number2):
    if (number1 > number2):
        print(f"{number1} is larger than {number2}.")
    elif (number2 > number1):
        print(f"{number2} is larger than {number1}.")
    else:
        print(f"{number1} and {number2} are equal.")


def main():
    
    # Prompts user to input numbers for calculator.
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter the second number: "))

    # Calls the add_two function.
    add_two(number1,number2)

    # Calls the multiply_two function.
    multiply_two(number1,number2)

    # Calls the divide_two function.
    divide_two(number1,number2)
    
    # Calls the subtract_two function.
    subtract_two(number1,number2)

    # Calls the remainder function.
    remainder(number1,number2)
    
    # Calls the power function.
    power(number1,number2)

    # Calls root function
    root(number1)

    # Calls bonus function - returns which number is larger.
    bonus(number1,number2)

# Calls test function
test()

main()




 