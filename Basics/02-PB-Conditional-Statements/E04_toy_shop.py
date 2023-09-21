# EXAM
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

# Вход
# От конзолата се четат 6 реда:
# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]

# Изход
# На конзолата се отпечатва:
# •	Ако парите са достатъчни се отпечатва:
# o	"Yes! {оставащите пари} lv left."
# •	Ако парите НЕ са достатъчни се отпечатва:
# o	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

trip_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

number_of_toys = puzzles_number + dolls_number + bears_number + minions_number + trucks_number
toys_total_price = puzzles_number * 2.60 + dolls_number * 3 + bears_number * 4.10 + minions_number * 8.20 + trucks_number * 2

if number_of_toys >= 50:
    toys_total_price = toys_total_price * 0.75

clear_profit = toys_total_price * 0.90

if trip_price <= clear_profit:
    remainder = clear_profit - trip_price
    print(f'Yes! {remainder:.2f} lv left.')
else:
    more = trip_price - clear_profit
    print(f'Not enough money! {more:.2f} lv needed.')


# diff = abs(total_sum - trip_price)
# if total_sum >= trip_price:
#     print(f"Yes! {diff:.2f} lv left.")
# else:
#     print(f"Not enough money! {diff:.2f} lv needed.")