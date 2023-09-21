# Деси има фризьорски салон в София. Тя всеки ден си поставя за цел да постигне определена печалба. Напишете програма,
# която изчислява дали е успяла да постигне целта за деня, като знаете следното:
# Деси ще приема клиенти докато не приключи работния ден. Ако постигне желания приход обаче, тя ще затвори салона.
# Когато клиент влезе ще може да си избере една от следните услуги:
# •	Подстригване (haircut):
# o	Мъжко (mens) - 15лв.
# o	Дамско (ladies) – 20лв.
# o	Детско (kids) – 10лв.
# •	Боядисване (color):
# o	Поддръжка (touch up) – 20лв.
# o	Пълно боядисване (full color) – 30лв.
# Вход:
# От конзолата първоначално се чете 1 ред:
# •	цел за деня – цяло число в интервала [1 … 5000]
# След това се четат поредица от редове до получаване на команда "closed" или докато Деси не постигне целта за
# деня – услугата, която иска клиентът – текст с възможности "haircut" и "color".
# При команда "haircut" ще се очаква да се въведе видът на подстригването – "mens", "ladies" или "kids".
# При команда "color" ще се очаква видът на боядисването – "touch up" или "full color".
# Изход:
# На конзолата се отпечатват 2 реда:
# •	На първия ред:
# o	Ако Деси е успяла да постигне целта за деня:
# "You have reached your target for the day!"
# o	Ако Деси не е успяла да постигне целта за деня:
# "Target not reached! You need {колко пари не и достигат, за да стигне целта}lv. more."
# •	На втория ред:
# 	"Earned money: {парите, които е спечелила за деня}lv."

goal = int(input())
total_earn = 0
input_line = input()
enough_money = False

while input_line != 'closed':
    action = input_line
    type_action = input()

    if action == 'haircut':
        if type_action == 'mens':
            total_earn += 15
        elif type_action == 'ladies':
            total_earn += 20
        elif type_action == 'kids':
            total_earn += 10
    elif action == 'color':
        if type_action == 'touch up':
            total_earn += 20
        elif type_action == 'full color':
            total_earn += 30

    if total_earn >= goal:
        enough_money = True
        break

    input_line = input()

if enough_money:
    print(f'You have reached your target for the day!')
else:
    diff = goal - total_earn
    print(f'Target not reached! You need {diff}lv. more.')

print(f'Earned money: {total_earn}lv.')
