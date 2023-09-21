# Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. Набелязва си определен
# брой филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
# Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният рейтинг
# от всички филми, които си е набелязала да гледа.
# Вход
# От конзолата първо се чете един ред:
# •	Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# •	Име на филма – текст
# •	Рейтинг на филма - реално число в интервала [1.00…10.00]
# Изход
# Отпечатват се три реда в следния формат:
# •	"{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
# •	"{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
# •	"Average rating: {средният рейтинг на всички филми}"
# Максималният, минималният и средният рейтинг да се форматира до първата цифра след десетичния знак.

import sys

films_number = int(input())

max_rating = - sys.maxsize
min_rating = sys.maxsize
film_max_rating = ''
film_min_rating = ''
sum_ratings = 0

for _ in range(1, films_number + 1):
    film_name = input()
    film_rating = float(input())
    sum_ratings += film_rating

    if film_rating < min_rating:
        min_rating = film_rating
        film_min_rating = film_name

    if film_rating > max_rating:
        max_rating = film_rating
        film_max_rating = film_name

average_rating = sum_ratings / films_number

print(f'{film_max_rating} is with highest rating: {max_rating:.1f}')
print(f'{film_min_rating} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')