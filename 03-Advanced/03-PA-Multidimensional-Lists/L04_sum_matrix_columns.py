# Write a program that reads a matrix from the console and prints the sum for each column
# on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}". On the
# next rows, you will get elements for each column separated with a single space.

rows, columns = [int(x) for x in input().split(', ')]
sum_columns = [0 for _ in range(columns)]

for _ in range(rows):
    current_row = [int(x) for x in input().split()]

    for i in range(columns):
        sum_columns[i] += current_row[i]

print(*sum_columns, sep='\n')

# row_count, col_count = [int(el) for el in input().split(", ")]
#
# matrix = []
#
# for _ in range(row_count):
#     row_data = [int(el) for el in input().split()]
#     matrix.append(row_data)
#
#
# for col_index in range(col_count):
#     col_sum = 0
#     for row_index in range(row_count):
#         col_sum += matrix[row_index][col_index]
#
#     print(col_sum)