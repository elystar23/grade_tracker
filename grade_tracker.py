def calculate_average():
    grades = []
    print("\nEnter your grades one by one. Type 'done' when finished.")
    while True:
        g = input("Grade: ")
        if g.lower() == "done":
            break
        try:
            grades.append(float(g))
        except ValueError:
            print("Please enter a number or 'done'.")
    if len(grades) == 0:
        print("No grades entered.")
        return None
    total = 0
    for g in grades:
        total += g
    avg = total / len(grades)
    print(f"\nYour average is: {avg:.2f}%")
    return avg


def needed_on_final(current_grade, final_weight, target_grade):
    fw = final_weight / 100
    cw = 1 - fw
    required = (target_grade - current_grade * cw) / fw
    return required


def analyze_grade(*args):
    if len(args) == 1:
        return args[0]
    elif len(args) == 2:
        current, target = args
        return target - current
    else:
        total = 0
        for n in args:
            total += n
        return total / len(args)


while True:
    print("\n--- Grade Calculator Menu ---")
    print("1. Calculate my average")
    print("2. What do I need on the final to pass")
    print("3. Analyze grades")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculate_average()

    elif choice == "2":
        print("\nEnter the information below:")
        current = float(input("Your current grade: "))
        final_weight = float(input("Final exam weight (percent): "))
        target = float(input("What overall grade you want: "))
        needed = needed_on_final(current, final_weight, target)
        if needed > 100:
            print(f"\nYou need {needed:.2f}%, which is above 100 — impossible.")
        elif needed < 0:
            print("\nYou already secured that grade — you need 0%.")
        else:
            print(f"\nYou need at least {needed:.2f}% on the final.")

    elif choice == "3":
        raw = input("\nEnter numbers separated by spaces: ")
        parts = raw.split()
        nums = []
        for p in parts:
            nums.append(float(p))
        result = analyze_grade(*nums)
        print(result)

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        
