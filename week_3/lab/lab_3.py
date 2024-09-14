################################
# Program Name: lab_3.py
# Author: Ethan Muhs
# Date: 9/14/2024
# Assignment: Module 3 - Lab 3
# Purpose: 
################################

# Function to plot bar graphs
def plotBars(data_list, plotsymbol):
# use a for loop to print 40 blank lines
    print("\n" * 5)
# this "clears" out the console window

# for each value in the list:
# print "value" number of plot symbols using string replication
    for i in range(len(data_list)):
        print(plotsymbol * data_list[i])
    
# Main Program
# Build a list of numbers between 1 and 50

theList = [5, 10, 15, 22, 28, 30, 35, 40, 45, 65, 50]

plotBars(theList, "*")
print("The data is:", theList)
print()

def bubbleSort(sorted_list):
    for outer_index in range(len(sorted_list)):
        for inner_index in range(0, len(sorted_list) - outer_index - 1):
            if sorted_list[inner_index] > sorted_list[inner_index + 1]:
                temp = sorted_list[inner_index]
                sorted_list[inner_index] = sorted_list[inner_index + 1]
                sorted_list[inner_index + 1] = temp
    plotBars(sorted_list, "*")

bubbleSort(theList)
    