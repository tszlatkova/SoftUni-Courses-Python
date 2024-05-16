# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

input_line = input()
students = []

while ':' in input_line:
    name, ID, course = input_line.split(':')
    students.append({'name': name, 'ID': ID, 'course': course})

    input_line = input()

course_to_search = input_line

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
