# Write a program that reads a matrix from the console and changes its values. On the
# first line, you will get the matrix's rows - N. You will get elements for each column
# on the following N lines, separated with a single space. You will be receiving commands
# in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the
# value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by
# the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is
# valid if both of the given indexes are in the range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != 'END':
    command_split = command.split()
    action = command_split[0]
    row, col, value = [int(command_split[i]) for i in range(1, 4)]

    if all(coord in range(0, n) for coord in (row, col)):
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    command = input()

for row in matrix:
    print(' '.join(str(el) for el in row))
