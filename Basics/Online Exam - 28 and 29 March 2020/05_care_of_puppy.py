# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно определено
# количество храна. Да се напише програма, която проверява дали количеството храна, което е закупено за кученцето,
# ще е достатъчно докато кученцето бъде осиновено.
# Вход
# От конзолата се прочитат:
# •	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# •	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко
# хранене - цяло число в интервала [10 …1000]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Ако количеството храна е достатъчно да се отпечата:
#  	"Food is enough! Leftovers: {останала храна} grams."
# •	Ако количеството храна не е достатъчно да се отпечата:
#  	"Food is not enough. You need {нужно количество храна} grams more."

bought_food = int(input())

bought_food = bought_food * 1000
input_line = input()
total_eaten_food = 0

while input_line != 'Adopted':
    eaten_food = int(input_line)
    total_eaten_food += eaten_food

    input_line = input()

diff = abs(bought_food - total_eaten_food)

if total_eaten_food <= bought_food:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')