# Write a program that reads a matrix from the console and finds the 2x2 top-left
# submatrix with the biggest sum of its values.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".  On the
# next rows, you will get elements for each column, separated with a comma and a space
# ", ".
# You should print the found submatrix and the sum of its elements, as shown in the
# examples.

from sys import maxsize

rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = -maxsize
sub_matrix = None

for row in range(rows-1):
    for col in range(columns-1):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        below_element = matrix[row+1][col]
        diagonal_element = matrix[row+1][col+1]
        current_sum = current_element + next_element + below_element + diagonal_element

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element],
                          [below_element, diagonal_element]]

if sub_matrix:
    for row in range(2):
        print(*sub_matrix[row], sep=' ')

print(max_sum)
