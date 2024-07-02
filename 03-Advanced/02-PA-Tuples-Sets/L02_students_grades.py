# Write a program that reads students' names and their grades and adds them to the student
# record.
# On the first line, you will receive the number of students – N. On the following N lines
# , you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade, formatted
# to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ...
# {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

number_students = int(input())
students_grades = {}

for _ in range(number_students):
    name, grade = tuple(input().split())

    if name not in students_grades:
        students_grades[name] = []

    students_grades[name].append(float(grade))

for name, grades in students_grades.items():
    avg_grade = sum(grades)/len(grades)
    print(f"{name} -> {' '.join([f'{g:.2f}' for g in grades])} (avg: {avg_grade:.2f})")
