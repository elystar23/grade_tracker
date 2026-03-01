def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

grades = []

while True:
    user_input = input("Enter a grade or type 'done': ")
    if user_input == "done":
        break
    grades.append(int(user_input))

average = calculate_average(grades)
print("Average grade:", average)
