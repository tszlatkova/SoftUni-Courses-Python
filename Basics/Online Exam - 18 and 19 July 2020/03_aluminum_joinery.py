# Фирма-производител на алуминиева дограма приема поръчки за изработката и монтаж със следния ценоразпис за един брой.
# Фирмата приема само поръчки на едро (над 10 бр.). В зависимост от поръчания брой дограми, фирмата прави различна
# отстъпка на своите клиенти.
# Фирмата предлага също и доставка на поръчките си срещу 60 лв.
# Размер	    Единична цена	        Отстъпка от цената
# 90X130	        110 лв.         	 Над 30 броя – 5%
#                                        Над 60 броя – 8%

# 100X150	        140 лв.	             Над 40 броя – 6%
#                                        Над 80 броя – 10%

# 130X180	        190 лв.	             Над 20 броя – 7%
#                                        Над 50 броя – 12%

# 200X300	        250 лв.	             Над 25 броя – 9%
#                                        Над 50 броя – 14%
#
# Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка (след като се начисли
# цената за доставка, ако има такава).
# При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"
# Вход:
# Потребителят въвежда 3 реда:
# 1.	Брой дограми – цяло число в интервала [0..1000];
# 2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# 3.	Начин на получаване – текст
# •	С доставка - "With delivery"
# •	Без доставка - "Without delivery"
# Изход:
# Извежда се едно число – стойността на поръчката, в следния формат:
# o	"{Обща стойност на поръчката} BGN"
# Резултатът да се форматира до втори знак след десетичната запетая.

quantity = int(input())
type_woodwork = input()
delivery = input()

total_price = 0
price_per_one = 0

if type_woodwork == '90X130':
    if quantity <= 30:
        price_per_one = 110
    elif 30 < quantity <= 60:
        price_per_one = 0.95 * 110
    else:
        price_per_one = 0.92 * 110
elif type_woodwork == '100X150':
    if quantity <= 40:
        price_per_one = 140
    elif 40 < quantity <= 80:
        price_per_one = 0.94 * 140
    else:
        price_per_one = 0.90 * 140
elif type_woodwork == '130X180':
    if quantity <= 20:
        price_per_one = 190
    elif 20 < quantity <= 50:
        price_per_one = 0.93 * 190
    else:
        price_per_one = 0.88 * 190
elif type_woodwork == '200X300':
    if quantity <= 25:
        price_per_one = 250
    elif 25 < quantity <= 50:
        price_per_one = 0.91 * 250
    else:
        price_per_one = 0.86 * 250

total_price = quantity * price_per_one

if delivery == 'With delivery':
    total_price += 60

if quantity > 99:
    total_price = 0.96 * total_price

if quantity < 10:
    print(f'Invalid order')
else:
    print(f'{total_price:.2f} BGN')