# Grade Tracker Project Proposal

## Project Overview
This Python Grade Tracker is an interactive program that allows a user to choose from a menu. The user can calculate their current average by entering grades until they type "done," or they can calculate what score they need on the final exam to reach a target overall grade. The program helps students understand their progress in a class.

## Use of a List or Collection
The program uses a Python list to store all grades entered by the user.

Example:
grades = []

This list allows the program to store multiple grades and process them together when calculating the average.

## Use of a Function
The program uses two functions:

1. calculate_average()  
   This function collects grades from the user, stores them in a list, uses a loop to total them, and calculates the average.

2. needed_on_final(current_grade, final_weight, target_grade)  
   This function calculates the score needed on the final exam to reach a desired overall grade.

## Use of a Loop
The program uses loops in two places:

1. A loop that allows the user to enter multiple grades until they type "done."
2. A main menu loop that keeps the program running until the user chooses to exit.

## How to Run the Program
1. Open the project in a Python environment.
2. Run grade_tracker.py.
3. Choose an option from the menu.
4. Follow the prompts to either calculate your average or find out what you need on the final exam.
