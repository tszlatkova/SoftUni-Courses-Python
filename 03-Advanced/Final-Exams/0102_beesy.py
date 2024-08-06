# You will be given an integer n for the size of the field with a square shape. On the
# next n lines, you will receive the rows of the field.
# •	Your bee will be placed in a random position, marked with the letter 'B'.
# •	There will be flowers with nectar which need to be pollinated on random positions,
# marked with a single digit.
# •	There will be a hive, marked with the letter 'H'.
# •	All of the empty positions will be marked with '-'.
# The bee will have 15 units of energy initially.
# A command is received each turn until the bee runs out of energy or reaches the hive.
# The bee must collect and take at least 30 units of nectar to the hive. This would be the
# required quantity to make honey successfully.
# Keep in mind that even if the needed amount of nectar is collected, but the hive is not
# reached the bee continues to move according to the commands.
# You will be given commands for the bee's movement. The commands will be: "up", "down",
# "left", and "right". The bee moves towards the given direction. With each move, the
# bee's energy decreases by 1 unit.
# •	If the bee leaves the field (goes out of the boundaries of the matrix) depending on
# the move command,
#  it will be moved to the opposite side of the field.
# Example: In a 3x3 matrix the bee is at position [1,2] and receives the command "right"
# it will be moved to position [1,0].
# •	If the bee moves to a flower (a position marked with a digit), it collects the nectar
# (the value of the digit is added to the total amount of collected nectar) the flower
# disappears and should be replaced by '-'.
# •	If the bee runs out of energy, and the total amount of collected nectar is less than
# 30 units, the program ends. The correct output should be printed on the Console.
# •	If the bee runs out of energy and the total amount of collected nectar is at least
# 30 units, the energy will be restored with the amount of the difference between the
# nectar collected up to this turn and the minimum required amount for making honey (30).
# The value of the collected nectar is dropped to 30 units. The energy can be restored
# only once.
# Example: Collected nectar is equal to 40 units. 40 – 30 = 10. The bee's energy is
# increased by 10, the nectar is decreased to 30 units.

# Hint: Check for zero energy after restoration.
# o	The next time the bee runs out of energy, the movement discontinues. The program ends.
# The correct output should be printed on the Console.
# •	If the bee reaches a position, marked with  'H', the hive is reached and the program
# ends.

# Hint: When reaching the hive with zero energy, the success will depend on the amount of
# the collected nectar.
# The correct output should be printed on the Console.

# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines contain the values for every matrix row.
# •	After that, you will get commands to move (each one on a new line).

# Output
# •	On the first line:
# o	If the bee reaches the hive with at least 30 units of nectar collected, print this
# message and stop the program:
# 	"Great job, Beesy! The hive is full. Energy left: {energy}"
# o	If the bee reaches the hive but has not succeeded in collecting at least 30 units of
# nectar:
# 	"Beesy did not manage to collect enough nectar."
# o	If the bee runs out of energy, before returning to the hive:
# 	"This is the end! Beesy ran out of energy."

# •	On the next lines.
# o	Print the final state of the matrix, with the last known position of the bee,
# marked with 'B'.

# Constraints
# •	The size of the square matrix (field) will be between [2…10].
# •	Only the letters 'B' and 'H' will be present in the matrix.
# •	The flowers with nectar are represented by single positive digits between [0…9].
# •	There will always be enough commands to finish the program.
# •	The bee will always have 15 units of energy initially.

n = int(input())
matrix = []

for i in range(n):
    matrix.append([char for char in input()])

    for j in range(n):
        if matrix[i][j] == 'B':
            b_row = i
            b_col = j

b_energy = 15
nectar = 0
out_of_energy = 0
hive_reached = False

directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}
command = input()

while b_energy > 0:
    r, c = b_row + directions[command][0], b_col + directions[command][1]

    if r == n:
        r = 0
    elif r == -1:
        r = n - 1
    if c == n:
        c = 0
    elif c == -1:
        c = n - 1

    if matrix[r][c].isdigit():
        nectar += int(matrix[r][c])
    elif matrix[r][c] == 'H':
        hive_reached = True

    b_energy -= 1
    matrix[r][c] = 'B'
    matrix[b_row][b_col] = '-'
    b_row = r
    b_col = c

    if hive_reached or (b_energy == 0 and nectar < 30):
        break
    elif b_energy == 0:
        if out_of_energy < 1:
            out_of_energy += 1
            b_energy += (nectar - 30)
            nectar = 30
        else:
            break

    command = input()

if hive_reached:
    if nectar >= 30:
        print(f'Great job, Beesy! The hive is full. Energy left: {b_energy}')
    else:
        print(f'Beesy did not manage to collect enough nectar.')
else:
    print(f'This is the end! Beesy ran out of energy.')

for row in matrix:
    print(''.join(row))

# Input 1
#
# 6
# B-----
# 111111
# ------
# 111111
# ------
# H-----
# down
# right
# right
# right
# right
# right
# down
# left
# left
# left
# left
# left
# down
# right
# right
# right
# right
# right
#
# Output 1
#
# This is the end! Beesy ran out of energy.
# ------
# ------
# ------
# --B111
# ------
# H-----
#
#
# Input 2
#
# 4
# B---
# 1991
# ----
# ---H
# down
# right
# right
# right
# down
# down
# left
#
# Output 2
#
# Beesy did not manage to collect enough nectar.
# ----
# ----
# ----
# ---B
#
#
# Input 3
#
# 4
# B999
# --5-
# ---H
# ----
# right
# right
# right
# down
# left
# left
# left
# left
# down
#
# Output 3
#
# Great job, Beesy! The hive is full. Energy left: 6
# ----
# ----
# ---B
# ----
