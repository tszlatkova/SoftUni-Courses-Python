# EXAM
#
# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този
# на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

# Вход
# Входът се състои от четири реда:
# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]

# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"

# Резултатът да се форматира до втория знак след десетичната запетая.

budget = float(input())
video_cards = int(input())
processor = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processor_price = processor * 0.35 * video_cards_price
ram_price = ram * 0.10 * video_cards_price

total_price = video_cards_price + processor_price + ram_price

if video_cards > processor:
    total_price = 0.85 * total_price

diff = abs(total_price - budget)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')