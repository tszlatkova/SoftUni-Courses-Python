# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите
# името на ученика, а на всеки следващ ред неговите годишни оценки. Ученикът преминава в следващия клас,
# ако годишната му оценка е по-голяма или равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива
# изключен и програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

student_name = input()

current_grade = 0
count_excluded = 0
total_grades = 0

while current_grade <= 12:
    grade = float(input())

    if grade < 4:
        count_excluded += 1

        if count_excluded > 1:
            current_grade += 1
            print(f'{student_name} has been excluded at {current_grade} grade')
            break

        continue

    else:
        total_grades += grade
        current_grade += 1

    if current_grade == 12:
        average_grade = total_grades / 12
        print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
        break
