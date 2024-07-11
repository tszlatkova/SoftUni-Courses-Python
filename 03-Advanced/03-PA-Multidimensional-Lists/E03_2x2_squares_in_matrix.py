# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows}
# {columns}". In the following rows, you will receive characters separated by a single
# space. Print the number of all square matrices you have found.

rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split(' '))

square_matrices = 0

for i in range(rows-1):
    for j in range(columns-1):
        current_el = matrix[i][j]
        next_el = matrix[i][j+1]
        below_el = matrix[i+1][j]
        diagonal_el = matrix[i+1][j+1]

        if current_el == next_el == below_el == diagonal_el:
            square_matrices += 1

print(square_matrices)
