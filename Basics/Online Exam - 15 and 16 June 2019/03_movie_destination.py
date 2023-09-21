# Режисьорът на голяма кино продукция иска да разбере дали бюджетът, който са му отпуснали ще стигне за заснемане
# на филма. Помогнете му, като напишете програма, която изчислява колко ще му струва да заснеме филма, като знаете
# колко излиза един снимачен ден. Цената за един ден се определя от сезона и дестинацията:
# Дестинация
# Сезон	Dubai	Sofia	London
# Winter	45 000 lv.	17 000 lv.	24 000 lv.
# Summer	40 000 lv.	12 500 lv.	20 250 lv.
# Съществуват следните данъчни облекчения/облагания:
# •	Ако дестинацията е Дубай – 30% отстъпка от крайната цена
# •	Ако дестинацията е София – цената се оскъпява с 25%
# Вход
# От конзолата се четат 4 реда:
# 1.	Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# 2.	Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# 3.	Сезон – текст, с възможности "Summer" и "Winter"
# 4.	Брой дни  – цяло число в диапазона [1… 40]
# Изход
# На конзолата да се отпечата един ред:
# •	Ако бюджета е достатъчен:
#      "The budget for the movie is enough! We have {остатък от бюджета} leva left!"
# •	  Ако бюджета НЕ е достатъчен:
#      "The director needs {нужна сума} leva more!"
# Резултатът да се закръгли до втората цифра след десетичния знак.

budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

if season == 'Winter':
    if destination == 'Dubai':
        price_per_day = 45000
    elif destination == 'Sofia':
        price_per_day = 17000
    elif destination == 'London':
        price_per_day = 24000
elif season == 'Summer':
    if destination == 'Dubai':
        price_per_day = 40000
    elif destination == 'Sofia':
        price_per_day = 12500
    elif destination == 'London':
        price_per_day = 20250

total_price = days * price_per_day

if destination == 'Dubai':
    total_price = total_price * 0.70
elif destination == 'Sofia':
    total_price = total_price * 1.25

diff = abs(total_price - budget)

if total_price <= budget:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')