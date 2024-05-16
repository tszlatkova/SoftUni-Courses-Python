# Напишете програма, която да изчислява, колко ще струва на един шофьор да напълни резервоара на
# автомобила си, като знаете – какъв тип гориво зарежда, каква е цената за литър гориво и дали разполага
# с карта за отстъпки. Цените на горивата са както следва:
# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво: 18 ст. за литър бензин,
# 12 ст. за литър дизел и 8 ст. за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.

# Вход
# Входът се чете от конзолата и се състои от 3 реда:
# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"

# Изход
# На конзолата трябва да се отпечата един ред.
# •	"{крайната цена на горивото} lv."

# Цената на горивото да бъде форматираната до втората цифра след десетичния знак.

type_fuel = str(input())
litre_fuel = float(input())
club_card = str(input())

total_price = 0

if type_fuel == 'Gas':
    if club_card == 'Yes':
        total_price = (0.93 - 0.08) * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')
    elif club_card == 'No':
        total_price = 0.93 * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')
elif type_fuel == 'Gasoline':
    if club_card == 'Yes':
        total_price = (2.22 - 0.18) * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')
    elif club_card == 'No':
        total_price = 2.22 * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')
elif type_fuel == 'Diesel':
    if club_card == 'Yes':
        total_price = (2.33 - 0.12) * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')
    elif club_card == 'No':
        total_price = 2.33 * litre_fuel
        if litre_fuel <= 20:
            print(f'{total_price:.2f} lv.')
        elif 20 < litre_fuel <= 25:
            total_price = 0.92 * total_price
            print(f'{total_price:.2f} lv.')
        else:
            total_price = 0.90 * total_price
            print(f'{total_price:.2f} lv.')