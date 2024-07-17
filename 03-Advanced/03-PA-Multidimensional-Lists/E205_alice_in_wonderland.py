# Alice is going to the mad tea party, to see her friends. On the way to the party, she
# needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square
# shape. On the following n lines, you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps
# on a number position, she collects the tea bags and increases the quantity with the
# corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands
# can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and
# she does not need to continue collecting. Otherwise, if she steps into the rabbit hole
# or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.

# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by
# a single space)
# •	On each of the following lines, you will be given a move command

# Output
# •	On the first line:
# o	If Alice steps into the rabbit hole or goes out of the territory, print:
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# •	On the following lines, print the matrix.

# Constraints
# •	Alice will always either go outside Wonderland or collect 10 bags of tea
# •	All the commands will be valid
# •	All of the given numbers will be valid integers in the range [0, 10]

n = int(input())
matrix = []

for row in range(n):
    matrix.append([x for x in input().split()])

    for col in range(n):
        if matrix[row][col] == 'A':
            a_row = row
            a_col = col
            matrix[a_row][a_col] = '*'

tea_bags = 0
outside = False
rabbit_hole = False

while tea_bags < 10:
    command = input()

    if command == 'up':
        if a_row - 1 >= 0:
            move_up = matrix[a_row-1][a_col]
            if move_up.isdigit():
                tea_bags += int(move_up)
            elif move_up == 'R':
                rabbit_hole = True

            a_row -= 1
        else:
            outside = True

    elif command == 'down':
        if a_row + 1 < n:
            move_down = matrix[a_row+1][a_col]
            if move_down.isdigit():
                tea_bags += int(move_down)
            elif move_down == 'R':
                rabbit_hole = True

            a_row += 1
        else:
            outside = True

    elif command == 'right':
        if a_col + 1 < n:
            move_right = matrix[a_row][a_col+1]
            if move_right.isdigit():
                tea_bags += int(move_right)
            elif move_right == 'R':
                rabbit_hole = True

            a_col += 1
        else:
            outside = True

    elif command == 'left':
        if a_col - 1 >= 0:
            move_left = matrix[a_row][a_col-1]
            if move_left.isdigit():
                tea_bags += int(move_left)
            elif move_left == 'R':
                rabbit_hole = True

            a_col -= 1
        else:
            outside = True

    if outside:
        print("Alice didn't make it to the tea party.")
        break
    elif rabbit_hole:
        matrix[a_row][a_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    matrix[a_row][a_col] = '*'

if not outside and not rabbit_hole:
    print("She did it! She went to the party.")

for row in matrix:
    print(' '.join(row))
