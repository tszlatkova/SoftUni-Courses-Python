# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted
# numbers on a single line, separated by a single space.

import re

input_line = input()

while input_line:
    pattern = r'\d+'
    numbers = re.findall(pattern, input_line)

    if numbers:
        print(' '.join(numbers), end = ' ')

    input_line = input()