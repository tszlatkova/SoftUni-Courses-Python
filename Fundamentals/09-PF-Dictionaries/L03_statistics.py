# You seem to be doing great at your first job, so your boss decides to give you as your next task something more
# challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing
# one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

in_stock = {}
input_line = input()

while input_line != 'statistics':
    item = input_line.split(': ')
    product = item[0]
    quantity = int(item[1])

    if product not in in_stock:
        in_stock[product] = quantity
    else:
        in_stock[product] += quantity

    input_line = input()

print(f'Products in stock:')

for (product, quantity) in in_stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(in_stock)}')
print(f'Total Quantity: {sum(in_stock.values())}')
