def gradeCalculate(satir):
    # Remove the newline character from the end
    line = satir[:-1]
    # Split the line into name and grades
    parts = line.split(':')

    student_name = parts[0]
    grades = parts[1].split(',')

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    # Calculate the average
    average = (grade1 + grade2 + grade3) / 3

    # Determine the letter grade
    if 90 <= average <= 100:
        letter = "AA"
    elif 85 <= average <= 89:
        letter = "BA"
    elif 80 <= average <= 84:
        letter = "BB"
    elif 75 <= average <= 79:
        letter = "CB"
    elif 70 <= average <= 74:
        letter = "CC"
    elif 65 <= average <= 69:
        letter = "DC"
    elif 60 <= average <= 64:
        letter = "DD"
    elif 50 <= average <= 59:
        letter = "FD"
    else:
        letter = "FF"

    return student_name + ": " + letter + "\n"


def read_averages():
    # Read and print the letter grades for each student
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(gradeCalculate(line))


def enter_grade():
    # Get student information and grades from user
    first_name = input('Student first name: ')
    last_name = input('Student last name: ')
    grade1 = input('Grade 1: ')
    grade2 = input('Grade 2: ')
    grade3 = input('Grade 3: ')

    # Save the grades to the file
    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(first_name + ' ' + last_name + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')


def save_grades():
    # Read grades, calculate letter grades, and save to results file
    with open('sinav_notlari.txt', "r", encoding="utf-8") as file:
        results = []

        for line in file:
            results.append(gradeCalculate(line))

    with open("results.txt", "w", encoding="utf-8") as file2:
        for result in results:
            file2.write(result)

while True:
    # Main menu
    action = input('1- Read Grades\n2- Enter Grade\n3- Save Grades\n4- Exit\n')

    if action == '1':
        read_averages()
    elif action == '2':
        enter_grade()
    elif action == '3':
        save_grades()
    else:
        break