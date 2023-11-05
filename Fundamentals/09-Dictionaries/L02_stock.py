# After you have completed your first task, your boss decides to give you another one right away. Now not only you have
# to keep track of the stock, but also you should answer customers if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space). On the following
# line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".

input_stock = input().split()
asked_products = input().split()

stock_dictionary = {}

for i in range(0, len(input_stock), 2):
    key = input_stock[i]
    value = int(input_stock[i+1])
    stock_dictionary[key] = value

for product in asked_products:
    if product in stock_dictionary:
        print(f'We have {stock_dictionary[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")