################################
# Program Name: triangles.py
# Author: Ethan Muhs
# Date: 9/10/2024
# Assignment: Module 3 - Assignment 1
# Purpose: This program takes a user input (must be positive) for the lengths of 3 sides of a triangle and returns whether the results form a
#          triangle and whether the triangle is a right, isoscelese, and/or equilateral.
################################

# Function to get a user input, ensure that it is a positive integer
def get_input():
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input > 0:
                return user_input
        except ValueError:
            pass
        print("Invalid input.  Please enter a positive integer.")

# Function to determine if the sides form a triangle; if so, return True, else return False
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("These sides form a triangle.")
        return True
    else:
        print("These sides do not form a triangle.")
        return False

# Function to determine the type of triangle
def triangle_type(a, b, c):
    if a == b and a == c:
        return print("This is an equilateral triangle.")
    elif a == b or a == c or b == c:
        return print("This is an isosceles triangle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return print("This is a right triangle.")
    else:
        return print("This is a scalene triangle.")

# Get user input for 3 sides of a triangle
input1 = get_input()
input2 = get_input()
input3 = get_input()

# Determine if the sides form a triangle
i = is_triangle(input1, input2, input3)

# If the sides form a triangle, determine the type of triangle
if i == True:
    triangle_type(input1, input2, input3)
