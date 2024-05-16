# На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и
# плащане с карта. Установени са следните правила за заплащане:
# •	Ако продуктът надвишава 100лв., за него не може да се плати в брой
# •	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
# •	Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
# •	При успешна транзакция: "Product sold!"
# •	При неуспешна транзакция: "Error in transaction!"
# •	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да
# приключи и на конзолата да се изпишат два реда:
# o	"Average CS: {средно плащане в кеш на човек}"
# o	"Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# •	При получаване на команда "End", да се изпише един ред:
# o	"Failed to collect required money for charity."

sum_sales = int(input())

current_sum = input()
total_sum = 0
number_of_transaction = 0
in_cash = 0
with_card = 0
enough_money = False
total_in_cash = 0
total_with_card = 0

while current_sum != 'End':
    current_sum = int(current_sum)
    number_of_transaction += 1

    if number_of_transaction % 2 == 0:
        if current_sum >= 10:
            print('Product sold!')
            with_card += 1
            total_sum += current_sum
            total_with_card += current_sum
        else:
            print('Error in transaction!')
    else:
        if current_sum <= 100:
            print('Product sold!')
            in_cash += 1
            total_sum += current_sum
            total_in_cash += current_sum
        else:
            print('Error in transaction!')

    if total_sum >= sum_sales:
        enough_money = True
        break

    current_sum = input()

if enough_money or total_sum >= sum_sales:
    average_in_cash = total_in_cash / in_cash
    average_with_card = total_with_card / with_card
    print(f'Average CS: {average_in_cash:.2f}')
    print(f'Average CC: {average_with_card:.2f}')
else:
    print('Failed to collect required money for charity.')