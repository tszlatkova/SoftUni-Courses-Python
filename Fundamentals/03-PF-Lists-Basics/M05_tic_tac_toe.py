# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print
# "Second player won". Otherwise, print "Draw!".
# Example
# Input	Output
# 2 0 1
# 0 1 0
# 1 0 2	First player won

# 0 1 0
# 2 2 2
# 1 0 0	Second player won

# 1 0 2
# 0 1 2
# 1 2 0	Draw!

first_line = [int(i) for i in input().split(' ')]
second_line = [int(i) for i in input().split(' ')]
third_line = [int(i) for i in input().split(' ')]

first_winner = False
second_winner = False

for i in range(3):  # Checking the columns

    if first_line[i] == second_line[i] == third_line[i] == 1:
        first_winner = True
        break
    elif first_line[i] == second_line[i] == third_line[i] == 2:
        second_winner = True
        break

if not first_winner or not second_winner:  # Checking the rows and the diagonals
    if first_line.count(1) == 3 or second_line.count(1) == 3 or third_line.count(1) == 3:
        first_winner = True
    elif first_line.count(2) == 3 or second_line.count(2) == 3 or third_line.count(2) == 3:
        second_winner = True
    elif (first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1) \
            or (first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1):
        first_winner = True
    elif (first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2) \
            or (first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2):
        second_winner = True

if first_winner:
    print('First player won')
elif second_winner:
    print('Second player won')
else:
    print('Draw!')