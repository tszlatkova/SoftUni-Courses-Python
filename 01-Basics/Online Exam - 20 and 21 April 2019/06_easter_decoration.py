# За великденските празници, магазин започва да продава три вида великденска украса – кошнички за яйца (basket),
# великденски венци (wreath) и шоколадови зайци (chocolate bunny). Вашата задача е да напишете програма, която да
# изчислява каква сметка трябва да плати всеки един клиент на магазина, като се има в предвид, че всеки клиент закупил
# четен брой продукти, ще получи 20% отстъпка от крайната цена. След като всички клиенти приключат с покупките, трябва
# да се отпечата средно по колко пари е похарчил всеки човек.
# Цените на продуктите са:
# •	кошничка за яйца (basket) – 1.50 лв.
# •	великденски венец (wreath) – 3.80 лв.
# •	шоколадов заек (chocolate bunny) – 7 лв.
# Вход
# От конзолата първоначално се чете един ред:
# •	Брои на клиентите в магазина – цяло число [1… 100]
# •	След това за всеки един клиент на нов ред до получаване на командата "Finish" се чете:
# o	Покупката която клиента е избрал – текст ("basket", "wreath" или "chocolate bunny")
# Изход
# •	При получаване на командата "Finish" да се отпечата един ред:
# o	"You purchased {броя на покупките} items for {крайната цена} leva."
# •	Накрая, след като всички клиенти приключат с покупките, да се отпечата на един ред
# o	"Average bill per client is: {средно аритметично на парите които е похарчил всеки един клиент} leva."
# Всички пари трябва да бъдат форматирани до втората цифра след десетичния знак.

clients = int(input())
total_income = 0

for _ in range(1, clients + 1):
    input_line = input()
    number_of_items = 0
    total_per_client = 0

    while input_line != 'Finish':
        item = input_line
        number_of_items += 1

        if item == 'basket':
            total_per_client += 1.50
        elif item == 'wreath':
            total_per_client += 3.80
        elif item == 'chocolate bunny':
            total_per_client += 7

        input_line = input()

    if number_of_items % 2 == 0:
        total_per_client = 0.80 * total_per_client

    total_income += total_per_client
    print(f'You purchased {number_of_items} items for {total_per_client:.2f} leva.')

print(f'Average bill per client is: {total_income / clients:.2f} leva.')