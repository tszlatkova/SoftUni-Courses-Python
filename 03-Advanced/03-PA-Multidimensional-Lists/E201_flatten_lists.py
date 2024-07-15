# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values
# from left to right as shown below

import re

input_string = input().split('|')

pattern = r'-?\d+\.?\d*'
matrix = []

for string in input_string:
    matrix.append(re.findall(pattern, string))

flatten_list = []

for row in range(len(matrix)-1, -1, -1):
    flatten_list.extend(matrix[row])

print(*flatten_list)

# Input 1
# 1 2 3 |4 5 6 |  7  88

# Output 1
# 7 88 4 5 6 1 2 3

# Input 2
# 7 | 4  5|1 0| 2 5 |3

# Output 2
# 3 2 5 1 0 4 5 7

# Input 3
# 1| 4 5 6 7  |  8 9

# Output 3
# 8 9 4 5 6 7 1
