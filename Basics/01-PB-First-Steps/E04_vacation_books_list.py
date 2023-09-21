# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. Понеже Жоро
# предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко часа на ден трябва да
# отделя, за да прочете необходимата литература.

# Вход
# От конзолата се четат 3 реда:
# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

from math import floor
book_pages = int(input())

if 1 <= book_pages <= 1000:
    pages_per_hour = int(input())
    if 1 <= pages_per_hour <= 1000:
        days_to_read_the_book = int(input())
        if 1 <= days_to_read_the_book <= 1000:
            hours_per_day = floor((book_pages/pages_per_hour)/days_to_read_the_book)
            print (hours_per_day)
        else:
            print("Invalid days to read the book!")
    else:
        print("Ivalid pages per hour!")
else:
    print("Invalid pages of the book!")