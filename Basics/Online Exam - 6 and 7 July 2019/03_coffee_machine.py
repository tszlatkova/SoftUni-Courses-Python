# Напишете софтуер, който да пресмята сметката на клиент, закупил определен брой от дадена напитка от кафемашина.
# 	                        Без захар	            Нормално	                Допълнително захар
# Еспресо	                0.90 лв./бр.	        1 лв. /бр.	                1.20 лв. /бр.
# Капучино	                1.00 лв. /бр.	        1.20 лв. /бр.	            1.60 лв. /бр.
# Чай	                    0.50 лв. /бр.	        0.60 лв. /бр.	            0.70 лв. /бр.

# Трябва да имате предвид следните отстъпки:
# •	При избрана напитка без захар има 35% отстъпка.
# •	При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка.
# •	При сума надвишава 15 лева, 20% отстъпка от крайната цена,
# Отстъпките се прилагат в реда на тяхното описване.

# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]
# Изход
# На конзолата трябва да се отпечата един ред:
# "You bought {брой напитки} cups of {напитка} for {крайна цена} lv."
# Цената да бъде форматирана до втората цифра след десетичния знак.

drink = input()
sugar = input()
quantity = int(input())

price_per_drink = 0
total_price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price_per_drink = 0.90 * 0.65
    elif sugar == 'Normal':
        price_per_drink = 1.00
    elif sugar == 'Extra':
        price_per_drink = 1.20

    if quantity >= 5:
        price_per_drink = price_per_drink * 0.75
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price_per_drink = 1.00 * 0.65
    elif sugar == 'Normal':
        price_per_drink = 1.20
    elif sugar == 'Extra':
        price_per_drink = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price_per_drink = 0.50 * 0.65
    elif sugar == 'Normal':
        price_per_drink = 0.60
    elif sugar == 'Extra':
        price_per_drink = 0.70

total_price = quantity * price_per_drink

if total_price > 15:
    total_price = total_price * 0.80

print(f'You bought {quantity} cups of {drink} for {total_price:.2f} lv.')