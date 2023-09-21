# Напишете програма, която да пресмята статистика на оценки от изпит. В началото програмата получава броят на
# студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да изпечата процента
# на студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средният
# успех на изпита.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"

students = int(input())

total_grades = 0
top, bellow_top_1, bellow_top_2, fail = 0, 0, 0, 0

for _ in range(1, students + 1):
    student_grade = float(input())
    total_grades += student_grade

    if student_grade >= 5:
        top += 1
    elif 4 <= student_grade <= 4.99:
        bellow_top_1 += 1
    elif 3 <= student_grade <= 3.99:
        bellow_top_2 += 1
    else:
        fail += 1

average_grade = total_grades / students

top_percentage = top / students * 100
bellow_top_1_percentage = bellow_top_1 / students * 100
bellow_top_2_percentage = bellow_top_2 / students * 100
fail_percentage = fail / students * 100

print(f'Top students: {top_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {bellow_top_1_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {bellow_top_2_percentage:.2f}%')
print(f'Fail: {fail_percentage:.2f}%')
print(f'Average: {average_grade:.2f}')