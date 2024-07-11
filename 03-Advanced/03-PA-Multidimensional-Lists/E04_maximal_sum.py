# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square
# with a maximum sum of its elements. There will be no case with two or more 3x3 squares
# with equal maximal sum.

# Input
# •	On the first line, you will receive the rows and columns in the format "{rows}
# {columns}" – integers in the range [1, 20]
# •	On the following lines, you will receive each row with its columns - integers,
# separated by a single space in the range [-20, 20]

# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the
# format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a
# single space
from sys import maxsize

rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

# print([sum(matrix[row]) for row in range(len(matrix))])
max_sum = -maxsize
max_sum_matrix = []

for i in range(rows-2):
    for j in range(rows-2):
        current_matrix = []
        for k in range(3):
            current_matrix.append([matrix[i+k][j], matrix[i+k][j+1], matrix[i+k][j+2]])

        current_sum = sum([sum(current_matrix[row]) for row in range(len(current_matrix))])

        if current_sum > max_sum:
            max_sum_matrix = current_matrix
            max_sum = current_sum

print(f"Sum = {max_sum}")

for row in max_sum_matrix:
    print(*row, sep=' ')