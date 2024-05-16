# Write a program that keeps the information about all_students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will
# be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the all_students with an average grade higher than or equal to
# 4.50.
# Print the final dictionary with all_students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

def only_good_students(dict_students: dict):

    """
    Keep only the all_students with an average grade higher than or equal to 4.50 and creates a dictionary not with
    all of student's grades but only with the average.
    """
    subset_students = {}

    for student in dict_students.keys():
        grades_student = dict_students[student]
        avg_grade = sum(grades_student)/len(grades_student)

        if avg_grade >= 4.50:
            subset_students[student] = avg_grade

    return subset_students


input_lines = int(input())
all_students = {}

for _ in range(input_lines):
    student_name = input()
    student_grade = float(input())

    if student_name not in all_students.keys():
        all_students[student_name] = []

    all_students[student_name].append(student_grade)

better_students = only_good_students(all_students)

for name, averageGrade in better_students.items():
    print(f'{name} -> {averageGrade:.2f}')
