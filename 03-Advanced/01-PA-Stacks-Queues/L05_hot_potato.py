# Hot Potato is a game in which children form a circle and toss a hot potato. The counting
# starts with the first kid. Every nth toss, the child holding the potato leaves the game.
# When a kid leaves the game, it passes the potato to the next kid. It continues until
# there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will
# receive kids' names, separated by a single space. On the second line, you will receive
# the nth toss (integer) in which a child leaves the game.
# Print every kid who is removed from the circle in the format "Removed {kid}". In the
# end, print the only kid left in the format "Last is {kid}".

from collections import deque

kids = deque(input().split())
n = int(input())
turn = 0

while len(kids) > 1:

    for i in range(n):
        kid_with_potato = kids.popleft()
        turn += 1

        if turn == n:
            print(f'Removed {kid_with_potato}')
            turn = 0
        else:
            kids.append(kid_with_potato)

print(f'Last is {kids.popleft()}')

# another option is kids.rotate(n-1)
