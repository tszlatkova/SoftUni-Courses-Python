# Туристическа агенция има нужда от система за изчисляване на дължимата сума при резервация.
# В зависимост от различните дестинации и различните пакети, цената е различна.
# Цените за ден са следните:
# Цена за ден	                Банско/Боровец	                            Варна/Бургас
# 	                        с екипировка	без екипировка	            със закуска 	без закуска
# 	                                100лв.	80лв	                         130лв. 	100лв.
# VIP отстъпка                      10%	    5%	                                12%	    7%

# Ако клиентът е заявил престой повече от 7 дни, получава единия ден безплатно.
# Вход
# От конзолата се четат 4 реда:
# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [-10000 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Когато потребителят е въвел всички данни правилно, отпечатваме:
# "The price is {цената, форматирана до втория знак}lv! Have a nice time!"
# •	Ако потребителят е въвел по-малко от 1 ден за престой, отпечатваме:
# "Days must be positive number!"
# •	Когато при въвеждането на града или вида на пакета се въведат невалидни данни, отпечатваме: "Invalid input!"

import sys

city = input()
package = input()
VIP = input()
days = int(input())

if days < 1:
    print('Days must be positive number!')
    sys.exit()

if package not in ["noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"] or \
        city not in ["Bansko",  "Borovets", "Varna", "Burgas"]:
    print('Invalid input!')
    sys.exit()

price_per_day = 0
total_price = 0

if city == 'Bansko' or city == 'Borovets':
    if package == 'noEquipment':
        if VIP == 'no':
            price_per_day = 80
        elif VIP == 'yes':
            price_per_day = 80 * 0.95
    elif package == 'withEquipment':
        if VIP == 'no':
            price_per_day = 100
        elif VIP == 'yes':
            price_per_day = 100 * 0.90
elif city == 'Varna' or city == 'Burgas':
    if package == 'noBreakfast':
        if VIP == 'no':
            price_per_day = 100
        elif VIP == 'yes':
            price_per_day = 100 * 0.93
    elif package == 'withBreakfast':
        if VIP == 'no':
            price_per_day = 130
        elif VIP == 'yes':
            price_per_day = 130 * 0.88

if days > 7:
    total_price = price_per_day * (days -1)
else:
    total_price = price_per_day * days

print(f'The price is {total_price:.2f}lv! Have a nice time!')


