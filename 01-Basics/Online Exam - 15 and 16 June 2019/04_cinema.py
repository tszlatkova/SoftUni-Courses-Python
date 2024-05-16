# От кино ви наемат да напишете програма, чрез която да разберете дали на една прожекцията ще се запълни залата и
# колко пари ще се изкарат от нея. Получавате места в залата и на всеки следващ ред до команда "Movie time!",
# колко хора влизат в залата. Цената на един билет е 5 лв. Ако текущия брой хора влезли в залата се дели на 3 без
# остатък, се прави отстъпка 5лв от общата им сметка.
# Ако в залата се опитат да влязат повече хора от колкото места са останали, то се счита че местата са изчерпани и
# програмата трябва да приключи четенето на вход.
# Вход
# От конзолата се четат:
# •	На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# o	Брой хора влизащи в киното - цяло число в интервала [1… 15]
# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Movie time!":
#  "There are {останали места} seats left in the cinema."
# •	При изчерпване на местата в залата:
# 	"The cinema is full."
# След това да се отпечата:
# 	"Cinema income - {приходи от залата} lv."

all_seats = int(input())

input_line = input()
total_profit = 0
all_seats_taken = False

while input_line != 'Movie time!':
    people_number = int(input_line)
    all_seats -= people_number

    if all_seats < 0:
        all_seats_taken = True
        break

    income = people_number * 5

    if people_number % 3 == 0:
        income -= 5

    total_profit += income

    input_line = input()

if all_seats_taken:
    print('The cinema is full.')
else:
    print(f'There are {all_seats} seats left in the cinema.')

print(f'Cinema income - {total_profit} lv.')