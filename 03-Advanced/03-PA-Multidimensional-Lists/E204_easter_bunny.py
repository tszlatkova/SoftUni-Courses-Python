# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. In the
# following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the
# maximum number of eggs. The directions that should be considered as possible are up,
# down, left, and right. If you reach a trap while checking some of the directions, you
# should not consider the fields after the trap in this direction. The bunny can move
# within the field and cannot go outside its boundaries. Do not consider negative indices
# as valid ones. For more clarifications, see the examples below.
# Note: In some directions, the collected eggs can happen to be zero or a negative number.

# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)

# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected

# Constraints
# •	There will NOT be two or more paths consisting of the same total amount of eggs.

n = int(input())
bunny_position = []
matrix = []

for row in range(n):
    matrix.append([x for x in input().split()])

    for col in range(n):
        if matrix[row][col] == 'B':
            b_row = row
            b_col = col
            bunny_position.append([row, col])

max_eggs = 0
best_direction = ''
best_route = []

if b_row - 1 >= 0:
    collected_eggs = 0
    positions = []
    for row in range(b_row-1, -1, -1):
        if matrix[row][b_col] != 'X':
            collected_eggs += int(matrix[row][b_col])
            positions.append([row, b_col])
        else:
            break

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = 'up'
        best_route = positions

if b_row + 1 < n:
    collected_eggs = 0
    positions = []
    for row in range(b_row + 1, n):
        if matrix[row][b_col] != 'X':
            collected_eggs += int(matrix[row][b_col])
            positions.append([row, b_col])
        else:
            break

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = 'down'
        best_route = positions

if b_col + 1 < n:
    collected_eggs = 0
    positions = []
    for col in range(b_col + 1, n):
        if matrix[b_row][col] != 'X':
            collected_eggs += int(matrix[b_row][col])
            positions.append([b_row, col])
        else:
            break

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = 'right'
        best_route = positions

if b_col - 1 >= 0:
    collected_eggs = 0
    positions = []
    for col in range(b_col - 1, -1, -1):
        if matrix[b_row][col] != 'X':
            collected_eggs += int(matrix[b_row][col])
            positions.append([b_row, col])
        else:
            break

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = 'left'
        best_route = positions

print(best_direction)
for direction in best_route:
    print(direction)
print(max_eggs)
