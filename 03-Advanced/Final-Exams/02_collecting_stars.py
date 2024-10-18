# Input
# •	On the first line you will receive an integer N representing the size of the square
# field (matrix NxN).
# •	On the next N lines you will get the field rows (each position separated by a single
# space)
# •	On each of the following lines, you will get a valid move command.
# Output
# At the end of the program:
# •	If the player won the game, print: "You won! You have collected 10 stars."
# •	If the player loses the game, print: "Game over! You are out of any stars."
# •	Next, print the player's final position: "Your final position is [{row_position},
# {column_position}]"
# •	Finally, print the matrix in its final state, each position separated by a single
# space. Remember to mark the player's final position with "P".
# Constraints
# •	There will always be enough commands to either win or lose the game.
# •	There will be no case in which less than 10 stars will be in the field.
# •	There will be no obstacle at the field's starting position (coordinates [0,0])
# •	All given symbols will be valid following the description.

n = int(input())

matrix = []
p_row, p_col = 0, 0
stars = 2
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    matrix.append([char for char in input().split(' ')])

    for col in range(n):
        if matrix[row][col] == 'P':
            p_row = row
            p_col = col

command = input()

while True:
    r, c = p_row + directions[command][0], p_col + directions[command][1]

    if r >= n or r < 0 or c >= n or c < 0:
        if matrix[0][0] == '*':
            stars += 1

        matrix[p_row][p_col] = '.'
        p_row, p_col = 0, 0
        matrix[0][0] = 'P'
    elif matrix[r][c] == '*':
        stars += 1
        matrix[r][c] = 'P'
        matrix[p_row][p_col] = '.'
        p_row = r
        p_col = c
    elif matrix[r][c] == '.':
        matrix[r][c] = 'P'
        matrix[p_row][p_col] = '.'
        p_row = r
        p_col = c
    elif matrix[r][c] == '#':
        stars -= 1

    if stars == 10 or stars == 0:
        break

    command = input()

if stars == 10:
    print('You won! You have collected 10 stars.')
else:
    print('Game over! You are out of any stars.')

print(f'Your final position is [{p_row}, {p_col}]')

for row in matrix:
    print(' '.join(str(char) for char in row))
