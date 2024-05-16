# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети
# може да стане това.

change = float(input())

change_coins = change * 100
count = 0

while change_coins > 0:
    if change_coins >= 200:
        change_coins -= 200
    elif change_coins >= 100:
        change_coins -= 100
    elif change_coins >= 50:
        change_coins -= 50
    elif change_coins >= 20:
        change_coins -= 20
    elif change_coins >= 10:
        change_coins -= 10
    elif change_coins >= 5:
        change_coins -= 5
    elif change_coins >= 2:
        change_coins -= 2
    elif change_coins >= 1:
        change_coins -= 1
    else:
        break

    count += 1

print(count)
