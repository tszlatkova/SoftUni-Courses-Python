# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each course,
# print the registered users.
# Input
# •	Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
# •	The product data is always delimited by " : "
# Output
# •	Print the information about each course in the following format:
# "{course_name}: {registered_students}"
# •	Print the information about each student in the following format:
# "-- {student_name}"

input_line = input()
courses = {}

while input_line != 'end':
    student_info = input_line.split(' : ')
    course_name = student_info[0]
    student_name = student_info[1]

    if course_name not in courses.keys():
        courses[course_name] = []

    courses[course_name].append(student_name)

    input_line = input()

for course in courses.keys():
    print(f'{course}: {len(courses[course])}')
    for student in courses[course]:
        print(f'-- {student}')
