# Write a program that calculates the total cost of bought furniture. You will be given information about each purchase
# on separate lines until you receive the command "Purchase". Valid information should be in the format:
# ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store
# the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re

input_line = input()

pattern = r'>>([A-Za-z]+)<<([0-9]+[\.?0-9]*)!([0-9]+)'
bought_items = []
total_price = 0

while input_line != 'Purchase':
    match = re.findall(pattern, input_line)
    if match:
        furniture, price, quantity = match[0][0], match[0][1], match[0][2]
        bought_items.append(furniture)
        total_price += float(price) * int(quantity)

    input_line = input()

print('Bought furniture:')

for item in bought_items:
    print(item)

print(f'Total money spend: {total_price:.2f}')
