# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Вход
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Изход
# Да се отпечата на конзолата 5 реда:
# •	1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# •	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до вторият знак след запетаята.

months = int(input())

water = 20
internet = 15

total_electricity = 0
total_water = months * water
total_internet = months * internet
total_others = 0

for _ in range(1, months + 1):
    electricity = float(input())
    total_electricity += electricity
    total_others += (electricity + water + internet) * 1.20

average_per_month = (total_internet + total_water + total_others + total_electricity) / months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {total_others:.2f} lv')
print(f'Average: {average_per_month:.2f} lv')