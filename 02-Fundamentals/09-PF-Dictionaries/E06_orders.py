# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a
# quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is
# different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep
# adding items. Finally, print all items with their names and the total price of each product.

# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.

# Output
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

products = {}
current_product = input()

while current_product != 'buy':
    current_product = current_product.split(' ')
    item = current_product[0]
    price = float(current_product[1])
    quantity = int(current_product[2])
    new_item = False

    if item not in products.keys():
        new_item = True
        products[item] = []
        products[item].append(price)
        products[item].append(quantity)

    if not new_item:
        if products[item][0] != price:
            products[item][0] = price

        products[item][1] += quantity

    current_product = input()

for item in products.keys():
    total_price_item = products[item][0] * products[item][1]
    print(f'{item} -> {total_price_item:.2f}')
