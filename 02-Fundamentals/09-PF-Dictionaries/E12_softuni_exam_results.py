# Judge statistics on the last Programing 02-Fundamentals exam were not working correctly, so you have the task of taking
# all the submissions and analyzing them properly. You should collect all the submissions and print the final results
# and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam
# finished". You should store each username and their submissions and points. If a student has two or more submissions
# for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you
# should remove the user from the contest but preserve his submissions in the total count of submissions for each
# language.

# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"

# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];

# Output
# •	Print the exam results for each participant
# •	After that, print each language in the format shown above
# •	Allowed working time / memory: 100ms / 16MB

input_line = input()

students_results = {}
languages = {}

while input_line != 'exam finished':
    student_info = input_line.split('-')
    username = student_info[0]

    if student_info[1] == 'banned':
        del(students_results[username])
    else:
        student_language = student_info[1]
        student_points = int(student_info[2])

        if username not in students_results.keys():
            students_results[username] = {student_language: student_points}
        else:
            if student_language not in students_results[username].keys() \
                    or students_results[username][student_language] < student_points:

                students_results[username][student_language] = student_points

        if student_language not in languages.keys():
            languages[student_language] = 0

        languages[student_language] += 1

    input_line = input()

print('Results:')
for student in students_results.keys():
    max_points = students_results[student][max(students_results[student])]
    print(f'{student} | {max_points}')

print('Submissions:')
for language, count in languages.items():
    print(f'{language} - {count}')
