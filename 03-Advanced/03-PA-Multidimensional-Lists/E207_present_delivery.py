# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for
# the size of the neighborhood with a square shape. On the following lines, you will
# receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house
# where children may live. If the cell has an "X" on it, that means there lives a naughty
# kid. Otherwise, if a nice kid lives there, the cell is marked with "V". There can also
# be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", and "right" with one position each time. These will
# be the commands that you receive. If he moves to a house with a nice kid, the kid
# receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a
# present. If the command sends Santa to a cell marked with "C", Santa eats cookies and
# becomes happy and extra generous to all the kids around him* (meaning all of them will
# receive presents - it doesn't matter if naughty or nice). If Santa has been to a house,
# the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this
# case, Santa doesn't move to these cells, or if he does, he returns to the cell where the
# cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should
# end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# •	On the first line, you are given the integer m - the count of presents
# •	On the second - integer n - the size of the neighborhood
# •	The following n lines hold the values for every row
# •	On each of the following lines you will get a command
# Output
# •	On the first line:
# o	If Santa runs out of presents, but there are still some nice kids left print: "Santa
# ran out of presents!"
# •	Next, print the matrix.
# •	In the end, print one of these messages:
# o	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# o	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."
# Constraints
# •	The size of the square matrix will be between [2…10].
# •	Santa's position will be marked with an 'S'.
# •	There will always be at least 1 nice kid.
# •	There won't be a case where the cookie is on the border of the matrix.

presents = int(input())
size_n = int(input())

neighborhood = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(size_n):
    neighborhood.append([x for x in input().split()])

    for col in range(size_n):
        if neighborhood[row][col] == 'S':
            s_row, s_col = row, col
        elif neighborhood[row][col] == 'V':
            nice_kids += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

command = input()

while command != 'Christmas morning':
    r, c = s_row + directions[command][0], s_col + directions[command][1]

    if 0 <= r < size_n and 0 <= c < size_n:
        if neighborhood[r][c] == 'V':
            presents -= 1
            nice_kids_gifted += 1

        elif neighborhood[r][c] == 'C':
            for direction in directions.values():
                next_r, next_c = r + direction[0], c + direction[1]
                if neighborhood[next_r][next_c] in ['V', 'X'] and presents > 0:
                    presents -= 1
                    if neighborhood[next_r][next_c] == 'V':
                        nice_kids_gifted += 1

                    neighborhood[next_r][next_c] = '-'

        neighborhood[s_row][s_col] = '-'
        neighborhood[r][c] = 'S'
        s_row, s_col = r, c

    if presents == 0:
        break

    command = input()

if presents == 0 and nice_kids != nice_kids_gifted:
    print(f'Santa ran out of presents!')

for row in neighborhood:
    print(' '.join(row))

if nice_kids == nice_kids_gifted:
    print(f'Good job, Santa! {nice_kids_gifted} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_kids_gifted} nice kid/s.')

# Input 1
#
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
#
# Output 1
#
# - - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.
#
# Input 2
#
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up
#
# Output 2
#
# Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.
