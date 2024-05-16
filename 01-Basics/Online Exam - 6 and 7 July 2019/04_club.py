# Времето се затопля и клубовете пускат обещаващи промоции. Напише програма, която да изчислява приходите на един
# клуб за вечерта и дали е достигната желаната печалба, като знаете следните условия: цената на един коктейл
# е дължината неговото име. Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката.
# Вход
# От конзолата се четат:
# •	На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# o	Име на коктейла – текст
# o	Брой на коктейлите за поръчката – цяло число в интервала [1… 50]
# Изход
# На конзолата първо да се отпечата един ред:
# •	При получена команда "Party!":
#  "We need {недостигаща сума} leva more."
# •	При достигане на желаната печалба:
# 	"Target acquired."
# След това да се отпечата:
# 	"Club income - {приходи от клуба} leva."
# Парите да бъдат форматирани до втората цифра след десетичния знак.

wished_profit = float(input())

input_line = input()
total_profit = 0
time_to_party = False

while input_line != 'Party!':
	cocktail_name = input_line
	cocktails = int(input())

	order_price = cocktails * len(cocktail_name)

	if order_price % 2 == 0:
		total_profit += order_price
	else:
		total_profit += order_price * 0.75

	if total_profit >= wished_profit:
		time_to_party = True
		break

	input_line = input()

if time_to_party or total_profit >= wished_profit:
	print('Target acquired.')
else:
	diff = wished_profit - total_profit
	print(f'We need {diff:.2f} leva more.')

print(f'Club income - {total_profit:.2f} leva.')