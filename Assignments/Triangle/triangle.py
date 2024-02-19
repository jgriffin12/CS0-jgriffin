'''
Name: Janet Griffin
Date: 2/14/2024
Due Date: 02/17/2024
Assignment: Triangle
Description: 
1. This program will prompt the user to enter three separate numbers to input as the sides of a triangle. 
2. The program will then calculate the area and perimeter of the triangle.  
'''

# Ask user to input 3 numbers (sides of triangle)
side_1 = float(input("Enter the first number = "))
side_2 = float(input("Enter the second number = "))
side_3 = float(input("Enter the third number = "))

# Formula to find Triangle Perimeter and print perimeter
perimeter = side_1 + side_2 + side_3
print("Perimeter of Triangle: ", perimeter)

# Formula to find area of triangle using Herons Formula and print area 
s = perimeter / 2
area = (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5
print("Area of Triangle: ", area)





