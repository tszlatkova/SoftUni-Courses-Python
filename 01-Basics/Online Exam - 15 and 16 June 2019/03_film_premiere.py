# За предстояща премиера на три известни продукции, местно кино ви наема да напишете софтуер, който да изчислява
# цената, която клиентите трябва да заплатят, според филма и пакета, който са избрали.
#                           	John Wick           	Star Wars	                Jumanji
# Напитка	                    12 лв./бр.	            18 лв. /бр.	                9 лв. /бр.
# Пуканки	                    15 лв. /бр.	            25 лв. /бр.                	11 лв. /бр.
# Меню	                        19 лв. /бр.         	30 лв. /бр.	                14 лв. /бр.
# Напишете програма, която изчислява цената, която трябва да се заплати, като имате в предвид следните отстъпки:
# •	При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
# •	При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
# •	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
# •	Трети ред - брой билети - цяло число в интервала [1… 30]
# Изход
# На конзолата трябва да се отпечата един ред:
# "Your bill is {крайна цена} leva."
# Цената да бъде закръглена до втората цифра след десетичния знак.

film_name = input()
menu_type = input()
tickets_number = int(input())

price_per_ticket = 0

if film_name == 'John Wick':
    if menu_type == 'Drink':
        price_per_ticket = 12
    elif menu_type == 'Popcorn':
        price_per_ticket = 15
    elif menu_type == 'Menu':
        price_per_ticket = 19
elif film_name == 'Star Wars':
    if menu_type == 'Drink':
        price_per_ticket = 18
    elif menu_type == 'Popcorn':
        price_per_ticket = 25
    elif menu_type == 'Menu':
        price_per_ticket = 30

    if tickets_number >= 4:
        price_per_ticket = 0.70 * price_per_ticket

elif film_name == 'Jumanji':
    if menu_type == 'Drink':
        price_per_ticket = 9
    elif menu_type == 'Popcorn':
        price_per_ticket = 11
    elif menu_type == 'Menu':
        price_per_ticket = 14

    if tickets_number == 2:
        price_per_ticket = 0.85 * price_per_ticket

bill = tickets_number * price_per_ticket

print(f'Your bill is {bill:.2f} leva.')