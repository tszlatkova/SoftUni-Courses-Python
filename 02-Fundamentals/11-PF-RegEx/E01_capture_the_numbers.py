# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re

input_line = input()

while input_line:
    pattern = r'\d+'
    numbers = re.findall(pattern, input_line)

    if numbers:
        print(' '.join(numbers), end=' ')

    input_line = input()

# Input 1
# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45

# Output 1
# 300 3 22 45

# Input 2
# 123a456
# 789b987
# 654c321
# 0
#
# Output 2
# 123 456 789 987 654 321 0

