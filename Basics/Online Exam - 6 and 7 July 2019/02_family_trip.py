# Задача 2.  Семейна почивка
# Семейство Иванови планират семейната си почивка. Вашата задача е да напишете програма, която да изчислява дали
# предвидения от тях бюджет ще им стигне, като знаете колко нощувки са планирали, каква е цената за нощувка и
# колко процента от бюджета са предвидили за допълнителни разходи. Трябва да се има предвид, че ако броят на
# нощувките е по-голям от 7, цената за нощувка се намаля с 5%.

# Вход
# От конзолата се четат 4 реда:
# •	Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# •	Брой нощувки – цяло число в интервала [0 … 1000]
# •	Цена за нощувка – реално число в интервала [1.00 … 500.00]
# •	Процент за допълнителни разходи – цяло число в интервала [0 … 100]

# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако сумата е достатъчна:
# o	"Ivanovi will be left with {останали пари след почивката} leva after vacation."
# •	Ако НЕ е достигната сумата:
# o	"{парите нужни до достигане на целта} leva needed."

# Сума трябва да се форматира до втората цифра след десетичния знак.

family_budget = float(input())
nights_number = int(input())
price_per_night = float(input())
percentage_budget = int(input())

total_price_nights = 0

if nights_number > 7:
    total_price_nights = 0.95*price_per_night*nights_number
elif 0 <= nights_number <= 7:
    total_price_nights = price_per_night*nights_number

percentage_more = family_budget*percentage_budget/100

trip_price = total_price_nights + percentage_more

if trip_price <= family_budget:
    remainder = family_budget - trip_price
    print(f'Ivanovi will be left with {remainder:.2f} leva after vacation.')
else:
    remainder = trip_price - family_budget
    print(f'{remainder:.2f} leva needed.')