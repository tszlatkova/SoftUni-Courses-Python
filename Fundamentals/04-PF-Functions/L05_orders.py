# Write a function that calculates the total price of an order and returns it. The function should receive one of the
# following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single
# piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
#
# Print the result formatted to the second decimal place.

def product_price(product, quantity):
    return {
        'coffee': 1.50 * quantity,
        'water': 1.00 * quantity,
        'coke': 1.40 * quantity,
        'snacks': 2.00 * quantity
    }.get(product)


product = input()
quantity = int(input())

total_price = product_price(product, quantity)

print(f'{total_price:.2f}')