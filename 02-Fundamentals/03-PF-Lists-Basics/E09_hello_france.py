# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you
# decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have
# to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items
# as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if
# the budget after selling all the items is enough for buying the train ticket.

# Input / Constraints
# •	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the
# range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]

# Output
# •	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following
# format:
# "{price1} {price2} {price3} … {priceN}"
# •	Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# •	Finally:
# o	If the budget is enough for buying the train ticket, print: "Hello, France!"
# o	Otherwise, print: "Not enough money."

input_line = input().split('|')
budget = float(input())

items = [input_line[i].split('->') for i in range(len(input_line))]

new_prices = []
profit = 0

for i in range(len(items)):
    current_price = float(items[i][1])

    if current_price <= budget:
        if (items[i][0] == 'Clothes' and current_price <= 50) \
                or (items[i][0] == 'Shoes' and current_price <= 35) \
                or (items[i][0] == 'Accessories' and current_price <= 20.50):
            budget -= current_price
            new_prices.append(current_price * 1.40)
            profit += current_price * 0.40
    else:
        continue

for item in new_prices:
    print(f'{item:.2f}', end=" ")
print()
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(new_prices)

if new_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

# I've use the function round() in line 48 but it wasn't right in the Judge system. Maybe because of this:

# The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the
# expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly
# as a float. See Floating Point Arithmetic: Issues and Limitations for more information

# https://softuni.bg/forum/30261/zadacha-9-hello-france

