# Write a program that reads a matrix from the console and performs certain operations
# with its elements. User input is provided similarly to the problems above - first, you
# read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}"
# where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the
# matrix. A valid command starts with the "swap" keyword along with four valid coordinates
# (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print
# the matrix at each step (thus, you will be able to check if the operation was performed
# correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more
# coordinates entered, or the given coordinates are not valid), print "Invalid input!"
# and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split(' ')])

command = input()

while command != 'END':
    command_split = command.split(' ')

    if len(command_split) != 5:
        print('Invalid input!')
        command = input()
        continue
    else:
        action = command_split[0]
        x1, y1, x2, y2 = [int(command_split[i]) for i in range(1, 5)]

        if action != 'swap':
            print('Invalid input!')
            command = input()
            continue
        else:
            if all(coord in range(0, rows) for coord in (x1, x2)) \
                    and all(coord in range(0, columns) for coord in (y1, y2)):
                first_element = matrix[x1][y1]
                second_element = matrix[x2][y2]

                matrix[x1][y1] = second_element
                matrix[x2][y2] = first_element

                for row in matrix:
                    print(' '.join(row))
            else:
                print('Invalid input!')
                command = input()
                continue

    command = input()
