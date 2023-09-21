# Напишете програма, която да изчислява броя на посетителите в един фитнес център. В началото програмата
# получава броя на посетителите на фитнеса и за всеки човек - дейността, която извършва във фитнеса.
# На края програмата трябва да отпечата броят трениращи за всяка една дейност ("Back", "Chest", 'Legs", "Abs")
# и броят клиенти, закупили продукт ("Protein shake", "Protein bar"). Също така - процентът трениращи
# (спрямо общия брой посетители) и процентът на клиентите, закупили продукт от фитнеса.
# Вход
# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
# •	На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# •	За всеки един посетител на отделен ред – дейността във фитнеса – текст ("Back", "Chest", "Legs", "Abs",
# "Protein shake" или "Protein bar")
# Изход
# Да се отпечатат на конзолата 8 реда, които съдържат следната информация:
# Ред 1 -	"{брой хора трениращи гръб} - back"
# Ред 2 -	"{брой хора трениращи гърди} - chest"
# Ред 3 -	"{брой хора трениращи крака} - legs"
# Ред 4 -	"{брой хора трениращи коремни мускули} - abs"
# Ред 5 -	"{брой хора закупили протеинов шейк} - protein shake"
# Ред 6 -	"{брой хора закупили протеинов блок} - protein bar"
# Ред 7 -	"{процент на хората дошли да тренират}% - work out"
# Ред 8 -	"{процент на хората дошли да купят протеин}% - protein"
# Всички проценти трябва да са форматирани до втората цифра след десетичния знак.

clients = int(input())
back, chest, legs, abs_body, shake, bar = 0, 0, 0, 0, 0, 0

for _ in range (1, clients + 1):
    workout_or_food = input()

    if workout_or_food == 'Back':
        back += 1
    elif workout_or_food == 'Chest':
        chest += 1
    elif workout_or_food == 'Legs':
        legs += 1
    elif workout_or_food == 'Abs':
        abs_body += 1
    elif workout_or_food == 'Protein shake':
        shake += 1
    elif workout_or_food == 'Protein bar':
        bar += 1

workout_percentage = (back + chest + legs + abs_body) / clients * 100
food_percentage = 100 - workout_percentage

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_body} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{workout_percentage:.2f}% - work out")
print(f"{food_percentage:.2f}% - protein")