################################
# Program Name: dist_travelled.py
# Author: Ethan Muhs
# Date: 9/10/2024
# Assignment: Module 3 - Assignment 2
# Purpose: This program takes a user input for the speed of a vehicle and the number of hours it has traveled and returns a table of the distance.
################################

# Function to get a vehicle speed, ensure that it is a positive integer or 0
def get_speed():
    while True:
        try:
            speed = int(input("Enter the speed of the vehicle in mph as a positive integer or 0: "))
            if speed >= 0:
                return speed
        except ValueError:
            pass
        print("Invalid input.  Please enter a positive speed as an integer or 0.")

# Function to get the number of hours the vehicle has traveled, ensure that it is a positive integer
def get_hours():
    while True:
        try:
            hours = int(input("Enter the number of hours the vehicle has traveled as a positive integer: "))
            if hours > 1:
                return hours
        except ValueError:
            pass
        print("Invalid input. Please enter a positive number of hours as an integer.")

# Function to calculate the distance the vehicle has traveled
def distance(speed, hours):
    print("Hour\tDistance Traveled")
    print("-------------------------")
    for i in range(1, int(hours) + 1):
        print(i, "\t", speed * i)

# Get user input for the speed of the vehicle
speed = get_speed()

# Get user input for the number of hours the vehicle has traveled
hours = get_hours()

# Calculate the distance the vehicle has traveled
distance(speed, hours)
