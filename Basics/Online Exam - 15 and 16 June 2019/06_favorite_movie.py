# Петък вечер е и се чудите кой филм да си пуснете да гледате. Решавате да напишете програма, която да избере това
# вместо вас. До команда "STOP" получавате заглавия на любими ваши филми. Най-добрият филм за вас ще бъде този,
# който има най-много точки. Точките се изчисляват като сбор от ASCII стойностите на символите в заглавието на филма.
# (няма да има случай, в който имаме два филма с равен брой точки)
# При изчислението на точките трябва да се има предвид следното:
# •	За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието на филма.
# •	За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на филма.
# Може да имате максимум 7 заглавия на филми.
# Вход
# От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
# •	Заглавие на филм  – текст;
# Изход
# На конзолата да се отпечата:
# •	Ако сте достигнали лимита от 7 филма трябва да отпечатате:
# "The limit is reached."
# Да се отпечата най-добрият филм за вас:
# "The best movie for you is {заглавие на филм} with {сума на символите} ASCII sum."

input_line = input()
count_films = 0
max_ASCII = 0
best_film = ''
enough_films = False

while input_line != 'STOP':
    film_name = input_line
    count_films += 1
    sum_ASCII = 0

    for letter in range(len(film_name)):

        if 97 <= ord(film_name[letter]) <= 122:
            sum_ASCII = sum_ASCII + ord(film_name[letter]) - 2 * len(film_name)
        elif 65 <= ord(film_name[letter]) <= 90:
            sum_ASCII = sum_ASCII + ord(film_name[letter]) - len(film_name)
        else:
            sum_ASCII += ord(film_name[letter])

    if max_ASCII < sum_ASCII:
        max_ASCII = sum_ASCII
        best_film = film_name

    if count_films == 7:
        enough_films = True
        break

    input_line = input()

if enough_films:
     print(f'The limit is reached.')

print(f'The best movie for you is {best_film} with {max_ASCII} ASCII sum.')
