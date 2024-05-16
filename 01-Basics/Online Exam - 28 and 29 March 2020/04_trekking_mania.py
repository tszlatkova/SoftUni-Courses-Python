# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на
# групата, катерачите ще изкачват различни върхове.
# •	Група до 5 човека– Мусала
# •	Група от 6 до 12 – Монблан
# •	Група от 13 до 25 – Килиманджаро
# •	Група от 26 до 40 – К2
# •	Група от 41 или повече – Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората
# цифра след десетичната запетая.
# •	Първи ред - процентът изкачващи Мусала
# •	Втори ред – процентът изкачващи Монблан
# •	Трети ред – процентът изкачващи Килиманджаро
# •	Четвърти ред – процентът изкачващи К2
# •	Пети ред – процентът изкачващи Еверест

groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_people = 0

for _ in range(1, groups + 1):
    group_number = int(input())
    total_people += group_number

    if group_number <= 5:
        musala_count += group_number
    elif 6 <= group_number <= 12:
        monblan_count += group_number
    elif 13 <= group_number <= 25:
        kilimanjaro_count += group_number
    elif 26 <= group_number <= 40:
        k2_count += group_number
    else:
        everest_count += group_number

musala_percentage = musala_count / total_people * 100
monblan_percentage = monblan_count / total_people * 100
kilimanjaro_percentage = kilimanjaro_count / total_people * 100
k2_percentage = k2_count / total_people * 100
everest_percentage = everest_count / total_people * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')