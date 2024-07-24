# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented
# as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with the symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands
# you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the
# given steps. You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your
# current position without moving). Beware that there might be targets that stand in the
# way of other targets, and you cannot reach them - you can shoot only the nearest target.
# When you have shot a target, the field becomes an empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training
# completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training
# not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the
# examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit,
# as shown in the examples.
# Constraints
# •	All the commands will be valid
# •	There will always be at least one target

matrix = []
targets = []
hit_targets = []

for row in range(5):
    matrix.append([x for x in input().split()])

    for col in range(5):
        if matrix[row][col] == 'A':
            a_row, a_col = row, col
        elif matrix[row][col] == 'x':
            targets.append([row, col])

number_commands = int(input())
no_targets = False
all_targets = len(targets)

for _ in range(number_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == 'move':
        steps = int(command[2])
        if direction == 'right':
            new_col = a_col + steps
            if new_col < 5 and matrix[a_row][new_col] == '.':
                a_col = new_col
        elif direction == 'left':
            new_col = a_col - steps
            if new_col >= 0 and matrix[a_row][new_col] == '.':
                a_col= new_col
        elif direction == 'up':
            new_row = a_row - steps
            if new_row >= 0 and matrix[new_row][a_col] == '.':
                a_row = new_row
        elif direction == 'down':
            new_row = a_row + steps
            if new_row < 5 and matrix[new_row][a_col] == '.':
                a_row = new_row
    elif action == 'shoot':
        if direction == 'right':
            if a_col + 1 < 5:
                for index in range(a_col+1, 5):
                    if matrix[a_row][index] == 'x':
                        matrix[a_row][index] = '.'
                        targets.remove([a_row, index])
                        hit_targets.append([a_row, index])
                        break
        elif direction == 'left':
            if a_col - 1 >= 0:
                for index in range(a_col-1, -1, -1):
                    if matrix[a_row][index] == 'x':
                        matrix[a_row][index] = '.'
                        targets.remove([a_row, index])
                        hit_targets.append([a_row, index])
                        break
        elif direction == 'up':
            if a_row - 1 >= 0:
                for index in range(a_row-1, -1, -1):
                    if matrix[index][a_col] == 'x':
                        matrix[index][a_col] = '.'
                        targets.remove([index, a_col])
                        hit_targets.append([index, a_col])
                        break
        elif direction == 'down':
            if a_row + 1 < 5:
                for index in range(a_row+1, 5):
                    if matrix[index][a_col] == 'x':
                        matrix[index][a_col] = '.'
                        targets.remove([index, a_col])
                        hit_targets.append([index, a_col])
                        break

    if len(targets) == 0:
        no_targets = True
        break

if no_targets:
    print(f'Training completed! All {all_targets} targets hit.')
else:
    print(f'Training not completed! {len(targets)} targets left.')

if hit_targets:
    for target in hit_targets:
        print(target)

# Input 1

# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1

# Output 1

# Training not completed! 3 targets left.
# [4, 1]

# Input 2
#
# . . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right
#
# Output 2
#
# Training completed! All 2 targets hit.
# [4, 1]
# [2, 2]
#
# Input 3
#
# . . . . .
# . . . . .
# . . x . .
# . . . . .
# . x . . A
# 3
# shoot down
# move right 2
# shoot left
#
# Output 3
#
# Training not completed! 1 targets left.
# [4, 1]
