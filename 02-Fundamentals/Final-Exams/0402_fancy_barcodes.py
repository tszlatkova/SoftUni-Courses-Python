# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# •	It is surrounded by a "@" followed by one or more "#"
# •	It is at least 6 characters long (without the surrounding "@" or "#")
# •	It starts with a capital letter
# •	It contains only letters (lower and upper case) and digits
# •	It ends with a capital letter
# Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
# Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
# Next, you have to determine the product group of the item from the barcode. The product group is obtained by
# concatenating all the digits found in the barcode. If there are no digits present in the barcode, the default product
# group is "00".

# Examples:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46

# Input
# On the first line, you will be given an integer n – the count of barcodes that you will be receiving next.
# On the following n lines, you will receive different strings.

# Output
# For each barcode that you process, you need to print a message.
# If the barcode is invalid:
# •	"Invalid barcode"
# If the barcode is valid:
# •	"Product group: {product group}"

import re


def search_for_number(string):
    number = ''
    number_is_found = False
    for character in string:
        if character.isdigit():
            number += character
            number_is_found = True

    if number_is_found:
        return number
    else:
        return '00'


pattern = r'((@#{1,})([A-Z])([A-Za-z0-9)]{4,})([A-Z])(@#{1,}))'

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    barcode = input()

    match = re.match(pattern, barcode)

    if match:
        middle_characters = match.group(3) + match.group(4) + match.group(5)

        if len(middle_characters) >= 6:
            string_to_search = match.group(4)
            product_group = search_for_number(string_to_search)

            print(f'Product group: {product_group}')
        else:
            print('Invalid barcode')

    else:
        print('Invalid barcode')