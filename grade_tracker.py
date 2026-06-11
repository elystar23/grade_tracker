# ---------------------------------------------------------
# FUNCTION: calculate_average()
# ---------------------------------------------------------
# Q3: This function asks the user for grades, stores them in a list,
#     converts them to floats, calculates the average, prints it,
#     and returns the average.
# Q4: This function does NOT accept parameters, so you cannot pass x or y.
#     It only uses user input.
# Q5: Possible errors:
#     - ValueError if user types letters instead of numbers (caught by try/except)
#     - KeyboardInterrupt if user stops program manually
#     - No grades entered → returns None (handled)
# Q6: User input behavior:
#     - "done" stops input
#     - letters cause error message
#     - blank input causes ValueError → caught
#     - spaces cause ValueError → caught
def calculate_average():

    grades = []  
    # Q1: Data type → list
    # Q2: Why? A list can store multiple grades and allows looping.

    print("\nEnter your grades one by one. Type 'done' when finished.")

    while True:  
        # Q1: Data type → loop control structure (not a variable)
        # Q2: Why? Needed to repeatedly ask for grades.
        g = input("Grade: ")  
        # Q1: Data type → string (input() always returns a string)
        # Q2: Why? User input always starts as a string.
        # Q6: If user types letters → handled below. If user types "done" → exits loop.

        if g.lower() == "done":  
            # Q6: User typing "done" ends grade entry.
            break

        try:
            grades.append(float(g))  
            # Q1: float(g) → float
            # Q2: Why? Grades can be decimals.
            # Q6: If user types letters → ValueError → except block runs.
        except ValueError:
            print("Please enter a number or 'done'.")
            # Q5: This catches invalid numeric input.
            continue

    if len(grades) == 0:
        # Q5: Prevents ZeroDivisionError later.
        print("No grades entered.")
        return None

    total = 0  
    # Q1: Data type → integer initially, becomes float as grades are added.
    # Q2: Why? Used as accumulator for summing grades.

    for g in grades:
        total += g  
        # Q1: g is float
        # Q2: Why? Needed for math operations.

    avg = total / len(grades)  
    # Q1: Data type → float
    # Q2: Why? Averages are decimal values.

    print(f"\nYour average is: {avg:.2f}%")
    return avg  
    # Q4: Returns a float average.


# ---------------------------------------------------------
# FUNCTION: needed_on_final()
# ---------------------------------------------------------
# Q3: This function calculates what score is needed on the final exam
#     to reach a target overall grade.
# Q4: If x or y is passed and they are not numbers → ValueError (in main loop).
# Q5: Possible errors:
#     - Division by zero if final_weight = 0
#     - Negative or >100 results are handled in main loop
def needed_on_final(current_grade, final_weight, target_grade):

    fw = final_weight / 100  
    # Q1: float
    # Q2: Converts percent to decimal.

    cw = 1 - fw  
    # Q1: float
    # Q2: Coursework weight is remainder after final exam weight.

    required = (target_grade - current_grade * cw) / fw  
    # Q1: float
    # Q2: Formula requires decimals.

    return required  
    # Q4: Returns float. If fw = 0 → division by zero error.


# ---------------------------------------------------------
# FUNCTION: analyze_grade()
# ---------------------------------------------------------
# Q3: This function behaves differently depending on how many numbers are passed:
#     - 1 number → returns it
#     - 2 numbers → returns difference (target - current)
#     - 3+ numbers → returns average
# Q4: If x or y is passed and they are not numeric → ValueError in main loop.
# Q5: Possible errors:
#     - If args is empty → division by zero (but main loop prevents empty input)
def analyze_grade(*args):
    # Q1: args → tuple
    # Q2: Why? Allows unlimited numbers to be passed.

    if len(args) == 1:
        return args[0]  
        # Q1: args[0] → float
        # Q2: Just returns the number.

    elif len(args) == 2:
        current, target = args  
        # Q1: floats
        # Q2: Needed for subtraction.
        return target - current

    else:
        total = 0  
        # Q1: integer initially, becomes float
        # Q2: Used to accumulate sum.

        for n in args:
            total += n  
            # Q1: n → float
            # Q2: Needed for math.

        return total / len(args)  
        # Q1: float
        # Q2: Average calculation.


# ---------------------------------------------------------
# MAIN PROGRAM LOOP
# ---------------------------------------------------------
# Q3: This loop displays a menu, takes user input, and calls the correct function.
# Q4: Passing x or y here refers to user typing invalid menu choices.
# Q5: Possible errors:
#     - ValueError from float() conversions
#     - Division by zero in needed_on_final()
#     - KeyboardInterrupt if user stops program
# Q6: User input behavior:
#     - Invalid menu choice → prints error
#     - Letters where numbers expected → crash unless caught
while True:
    print("\n--- Grade Calculator Menu ---")
    print("1. Calculate my average")
    print("2. What do I need on the final to pass")
    print("3. Analyze grades")
    print("4. Exit")

    choice = input("Choose an option: ")  
    # Q1: string
    # Q2: Menu choices are text-based.
    # Q6: If user types letters or numbers not 1–4 → handled below.

    if choice == "1":
        calculate_average()

    elif choice == "2":
        print("\nEnter the information below:")

        current = float(input("Your current grade: "))  
        # Q1: float
        # Q2: Needed for math.
        # Q6: If user types letters → ValueError.

        final_weight = float(input("Final exam weight (percent): "))  
        # Q1: float
        # Q2: Needed for percent → decimal conversion.
        # Q5: If user types 0 → division by zero later.

        target = float(input("What overall grade you want: "))  
        # Q1: float
        # Q2: Needed for math.

        needed = needed_on_final(current, final_weight, target)  
        # Q4: If inputs invalid → error already occurred above.

        if needed > 100:
            print(f"\nYou need {needed:.2f}%, which is above 100 — impossible.")
        elif needed < 0:
            print("\nYou already secured that grade — you need 0%.")
        else:
            print(f"\nYou need at least {needed:.2f}% on the final.")

    elif choice == "3":
        raw = input("\nEnter numbers separated by spaces: ")  
        # Q1: string
        # Q2: Needed to split into parts.
        # Q6: If user types letters → float() fails later.

        parts = raw.split()  
        # Q1: list of strings
        # Q2: Splitting input creates list elements.

        nums = []  
        # Q1: list
        # Q2: Stores converted floats.

        for p in parts:
            nums.append(float(p))  
            # Q1: float
            # Q2: Needed for math.
            # Q6: If user types letters → ValueError.

        result = analyze_grade(*nums)  
        # Q4: Passing x or y here means invalid numeric input → error above.

        print(result)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")  
        # Q6: Handles any input not 1–4.
