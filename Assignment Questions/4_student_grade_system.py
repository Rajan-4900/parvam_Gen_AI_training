# This program implements a student grade system that allows users to input student details, 
# calculate their average marks, determine their grade, and display the information in a structured format. 
# It also calculates the sum of digits of the roll number for each student. 
# The program uses lists, sets, and dictionaries to manage and store data effectively.

# Student Grade System

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# Function to calculate sum of digits of roll number
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total


# Main function
def student_system():
    students = []   # list
    subjects = set()  # set (unique subjects)
    student_data = {}  # dictionary

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nEnter details for student", i+1)

        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))

        marks_list = []
        total = 0

        m = int(input("Enter number of subjects: "))

        for j in range(m):
            sub = input("Enter subject name: ")
            marks = int(input("Enter marks: "))

            subjects.add(sub)  # set
            marks_list.append(marks)  # list
            total += marks

        avg = total / m
        grade = calculate_grade(avg)

        # store in dictionary
        student_data[roll] = {
            "name": name,
            "marks": marks_list,
            "average": avg,
            "grade": grade,
            "roll_sum": sum_of_digits(roll)
        }

        students.append(name)

    # Display data
    print("\n--- Student Report ---")
    for roll, data in student_data.items():
        print("\nRoll:", roll)
        print("Name:", data["name"])
        print("Marks:", data["marks"])
        print("Average:", data["average"])
        print("Grade:", data["grade"])
        print("Sum of digits (Roll):", data["roll_sum"])

    print("\nAll Students:", students)
    print("Subjects Offered:", subjects)


# Run program
student_system()