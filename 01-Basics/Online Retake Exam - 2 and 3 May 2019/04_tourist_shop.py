# Времето се затопля и туристи, започват да си правят разходки високо в планината, където все още сняг, като за целта
# те трябва да закупят нужната туристическа екипировка.
# Вашата задача е да напишете програма, която да изчислява, стойността на екипировката, както и дали определения бюджет
# е достатъчен или не, като се знае, че в магазина има следната промоция: Всеки трети продукт е на половин цена.
# Вход
# От конзолата се чете:
# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт,
# чиято стойност е по-висока от наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]
# Изход
# На конзолата да се отпечатат следните редове според случая:
# •	При получаване на командата "Stop", на един ред:
# o	"You bought {брой на закупените продукти} products for {цена на покупките} leva."
# •	При заявка за покупка на продукт, чиято цена е по-висока от останалите пари, на два реда:
# o	"You don't have enough money!"
# o	"You need {недостигащи пари} leva!"

budget = float(input())

input_line = input()
product_count = 0
total_price = 0
no_more_budget = False

while input_line != 'Stop':
    product_name = input_line
    product_price = float(input())
    product_count += 1

    if product_count % 3 == 0:
        product_price = product_price * 0.50

    budget -= product_price

    if budget < 0:
        no_more_budget = True
        break

    total_price += product_price
    input_line = input()

if no_more_budget:
    print(f"You don't have enough money!")
    print(f'You need {abs(budget):.2f} leva!')
else:
    print(f'You bought {product_count} products for {total_price:.2f} leva.')