# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете
# програма, която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет
# ще им е достатъчен. Различните цветя са с различни цени:

# цвете              	Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	 5	     3.80	2.80	  3	      2.50

# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.

# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен -
# "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

flowers_type = input()
flowers_number = int(input())
budget = int(input())

total_price = 0

if flowers_type == 'Roses':
    total_price = flowers_number * 5
    if flowers_number > 80:
        total_price = total_price * 0.90
elif flowers_type == 'Dahlias':
    total_price = flowers_number * 3.80
    if flowers_number > 90:
        total_price = total_price * 0.85
elif flowers_type == 'Tulips':
    total_price = flowers_number * 2.80
    if flowers_number > 80:
        total_price = total_price * 0.85
elif flowers_type == 'Narcissus':
    total_price = flowers_number * 3
    if flowers_number < 120:
        total_price = flowers_number * 3 * 1.15
elif flowers_type == 'Gladiolus':
    total_price = flowers_number * 2.50
    if flowers_number < 80:
        total_price = flowers_number * 2.50 * 1.20

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {flowers_number} {flowers_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')