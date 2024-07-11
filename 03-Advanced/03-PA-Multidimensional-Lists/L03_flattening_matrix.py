# Write a program that receives a matrix and prints its flattened version (a list with all
# the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1,
# 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. On the next rows, you
# will get the elements for each column separated with a comma and a space ", ".

rows_number = int(input())

flattened_matrix = []

for _ in range(rows_number):
    current_elements = [int(x) for x in input().split(', ')]
    for el in current_elements:
        flattened_matrix.append(el)

print(flattened_matrix)

# rows_number = int(input())
#
# flattened_matrix = []
#
# for _ in range(rows_number):
#     flattened_matrix.extend([int(x) for x in input().split(', ')])
#
# print(flattened_matrix)
