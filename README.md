# Grade Tracker Project Proposal

## Project Overview
This Python Grade Tracker is an interactive program that allows a user to choose from a menu. The user can calculate their current average by entering grades until they type "done," calculate what score they need on the final exam to reach a target overall grade, or analyze a set of numbers using a function that accepts arguments. The program helps students understand their progress in a class and provides flexible tools for working with grade data.

## Use of a List or Collection
The program uses Python lists in multiple places:

- A list stores all grades entered by the user when calculating an average.
- A list stores numbers entered for the argument-based analysis function.

Examples:
grades = []
nums = []

These lists allow the program to store multiple values and process them together.

## Use of Functions
The program uses three functions:

1. calculate_average()
   This function collects grades from the user, stores them in a list, uses a loop to total them, and calculates the average.

2. needed_on_final(current_grade, final_weight, target_grade)
   This function accepts three arguments and calculates the score needed on the final exam to reach a desired overall grade.

3. analyze_grade(*args)
   This function accepts one or more arguments and returns a result based on how many values are provided. It demonstrates argument handling, looping, and working with collections.

## Use of Loops
The program uses loops in several places:

1. A loop that allows the user to enter multiple grades until they type "done."
2. A loop that totals the grades to compute the average.
3. A loop that processes numbers entered for the argument-based function.
4. A main menu loop that keeps the program running until the user chooses to exit.

## How to Run the Program
1. Open the project in a Python environment.
2. Run grade_tracker.py.
3. Choose an option from the menu.
4. Follow the prompts to calculate your average, determine what you need on the final exam, or analyze a set of numbers.
