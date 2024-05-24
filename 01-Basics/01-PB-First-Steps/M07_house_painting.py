# Напишете програма, която да пресмята колко литра боя е нужна за боядисването на къщa. Като за стените
# се използва зелена боя, а за покрива – червена. Разхода на зелената боя е 1 литър за 3.4 м2,
# а на червената – 1 литър за 4.3 м2.

# Стените имат следните размери:
# •	Предната и задната стена са квадрати със страна „x“
# o	на предната стена има правоъгълна врата с широчина 1.2м и височина 2м
# •	Страничните стени са правоъгълници със страни „x“ и „y“
# o	и на двете странични стени има по един квадратен прозорец със страна 1.5м

# Покривът има следните размери:
# •	Два правоъгълника със страни „x“ и „y“
# •	Два равностранни триъгълника със страна „x“ и височина „h“

# Трябва да пресметнете площта на всички страни и площта на покрива, за да
# намерите колко литра от всяка боя ще са нужни.

# Вход
# От конзолата се четат 3 реда:
# 1.	x – височината на къщата – реално число в интервала [2...100]
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]

# Изход
# Да се отпечатат на конзолата две числа всяко на нов ред:
# •	Литрите зелена боя
# •	Литритe червена боя

# Форматирани до вторият знак след десетичната запетая.

x = float(input())
y = float(input())
h = float(input())

windows_door_area = 1.2 * 2 + 2 * 1.5 * 1.5
green_area = 2*(x**2) + 2*y*x - windows_door_area
red_area = 2 * (x*h/2 + x*y)

green_paint = green_area/3.40
red_paint = red_area/4.30

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')