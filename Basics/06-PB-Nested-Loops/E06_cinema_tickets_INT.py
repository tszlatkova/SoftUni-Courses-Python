# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента
# от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o	Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# •	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# •	При получаване на командата "Finish" да се отпечатат четири реда:
# o	"Total tickets: {общият брой закупени билети за всички филми}"
# o	"{процент на студентските билети}% student tickets."
# o	"{процент на стандартните билети}% standard tickets."
# o	"{процент на детските билети}% kids tickets."

input_line = input()

student_count = 0
standard_count = 0
kids_count= 0
total_seats = 0
no_more_people = False

while input_line != 'Finish':
    film_name = input_line
    seats = int(input())

    input_seat = input()
    total_taken_seats = 0

    while input_seat != 'End':
        if input_seat == 'Finish':
            no_more_people = True
            break

        type_seat = input_seat

        if type_seat == 'student':
            student_count += 1
        elif type_seat == 'standard':
            standard_count += 1
        elif type_seat == 'kid':
            kids_count += 1

        total_taken_seats += 1

        if total_taken_seats == seats:
            break

        input_seat = input()

    taken_percentage_for_the_movie = total_taken_seats / seats * 100
    print(f'{film_name} - {taken_percentage_for_the_movie:.2f}% full.')

    total_seats += total_taken_seats

    if no_more_people:
        break

    input_line = input()

if student_count != 0:
    student_tickets_percentage = student_count / total_seats * 100
else:
    student_tickets_percentage = 0

if standard_count != 0:
    standard_tickets_percentage = standard_count / total_seats * 100
else:
    standard_tickets_percentage = 0

if kids_count != 0:
    kids_tickets_percentage = kids_count / total_seats * 100
else:
    kids_tickets_percentage = 0

print(f'Total tickets: {total_seats}')
print(f'{student_tickets_percentage:.2f}% student tickets.')
print(f'{standard_tickets_percentage:.2f}% standard tickets.')
print(f'{kids_tickets_percentage:.2f}% kids tickets.')