# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка
# или равна на 4.
# Вход
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]
# Изход
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

not_good_grades = int(input())

count_not_good_grades = 0
total_grades = 0
average_grade = 0
final_problem = ''
count_problems = 0

while True:
    name_problem = input()

    if name_problem == 'Enough':
        average_grade = total_grades / count_problems
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {count_problems}')
        print(f'Last problem: {final_problem}')
        break

    grade_problem = int(input())
    final_problem = name_problem

    if grade_problem <= 4:
        count_not_good_grades += 1

        if count_not_good_grades == not_good_grades:
            print(f'You need a break, {count_not_good_grades} poor grades.')
            break

    total_grades += grade_problem
    count_problems += 1

# flag = False
# count_poor = 0
# sum_grades = 0
# count_grades = 0
# last_problem = ""
# input_line = input()
# while input_line != "Enough":
#     current_grade = int(input())
#     if current_grade <= 4:
#         count_poor += 1
#
#     if count_poor == number_poor_grades:
#         flag = True
#         break
#
#     count_grades = count_grades + 1
#     sum_grades = sum_grades + current_grade
#     last_problem = input_line
#
#     input_line = input()
#
# if flag:
#     print(f"You need a break, {count_poor} poor grades.")
# else:
#     avg_grade = sum_grades / count_grades
#     print(f"Average score: {avg_grade:.2f}")
#     print(f"Number of problems: {count_grades}")
#     print(f"Last problem: {last_problem}")