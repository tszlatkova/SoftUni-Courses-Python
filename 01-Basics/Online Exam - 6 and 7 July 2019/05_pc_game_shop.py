# Магазин за компютърни игри ви наема за да направите статистика на процента продажби на игрите от
# последния месец, като изчислите по колко процента от общите продажби са за някоя от игрите.
# Процентите трябва да бъдат разделени на четири части, три заглавия на игри и всички останали :
# •	Hearthstone
# •	Fornite
# •	Overwatch
# •	Others
# Вход
# От конзолата се четат:
# •	Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o	Име на игра - текст
# Изход
# На конзолата да се изпишат четири реда:
# 	"Hearthstone - {процент продажби на Hearthstone}%"
# 	"Fornite - {процент продажби на Fornite}%"
# 	"Overwatch - {процент продажби на Overwatch}%"
# 	"Others - {процент продажби на всички останали игри}%"
# Резултатът да бъде закръглен до втората цифра след десетичния знак.

games_number = int(input())

hearthstone_sales = 0
fornite_sales = 0
overwatch_sales = 0
others_sales = 0

for _ in range(1, games_number + 1):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_sales += 1
    elif game_name == 'Fornite':
        fornite_sales += 1
    elif game_name == 'Overwatch':
        overwatch_sales += 1
    else:
        others_sales += 1

hearthstone_percentage = hearthstone_sales / games_number * 100
fornite_percentage = fornite_sales / games_number * 100
overwatch_percentage = overwatch_sales / games_number * 100
others_percentage = others_sales / games_number * 100

print(f'Hearthstone - {hearthstone_percentage:.2f}%')
print(f'Fornite - {fornite_percentage:.2f}%')
print(f'Overwatch - {overwatch_percentage:.2f}%')
print(f'Others - {others_percentage:.2f}%')