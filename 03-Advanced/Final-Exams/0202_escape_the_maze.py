# You are a brave traveler that got lost in a maze and you need to find your way out.
# The maze is represented by a matrix - field. Each cell in the field represents a part
# of the maze, and it can contain one of the following elements:
# •	'P' - Represents the starting position of the traveller.
# •	'X' - Represents the location of the exit that leads outside of the maze.
# •	'M' - Represents a monster which wants to harm the traveller.
# •	'H' - Represents a health potion which will restore the health of the traveller.
# •	'-' – Represents the maze's corridors, which the traveller can walk through.
# Initially, you will be given N – an integer, indicating the size of a square matrix.
# The traveller starts with 100 units of health.
# The traveller must carefully navigate through the maze, following the commands that
# will be received on each of the following lines- "up", "down", "right", and "left",
# moving one position towards the direction given. If the command leads the traveller
# outside the bounds of the field, skip the command and proceed with the next one.
# However, in the maze, encountering a cell marked with 'M' signifies the presence of a
# monster. When the traveller encounters a monster, he takes substantial damage, his
# health is reduced by 40 units. It's important to note that the monster disappears from
# the maze only if the traveller survives the encounter. In the case where the traveller's
# health drops to 0 or below due to the encounter with a monster, the traveller is
# considered defeated, health is set to zero and the maze traversal concludes. If the
# traveller survives, the monster disappears from the maze, and its position is marked
# with '-'. This indicates that the monster has been successfully dealt with and is no
# longer a threat in the subsequent maze traversal.
# In addition, within the maze, encountering a cell marked with 'H' signifies the presence
# of a health potion. When the traveller encounters a health potion, he moves in that
# direction and experiences a boost in his health by 15 units. It's crucial to note that
# the traveller's health may happen to exceed the maximum limit of 100 units during the
# adventure. If the traveller's health surpasses 100 units due to the health potion, it
# is adjusted to the maximum limit of 100 units. This ensures that the traveller's health
# does not exceed the predefined maximum value. The position is marked with '-'.
# Once the traveller successfully reaches a position marked as 'X', he finally reaches
# the exit and escapes the maze. The adventure is over.
# Remember, the traveller must follow the commands, he will always either reach the exit
# or die in the maze.
# In the end, print the final state of the matrix (maze area) with the traveller in his
# ending position. Each row is on a new line.

# Input
# •	On the first line, you will get N - the size of the matrix (square).
# •	On the next N lines, you will receive strings, representing each row of the matrix.
# •	On each of the following lines, you will receive the possible directions for the
# traveller to move - "up", "down", "right", and "left".

# Output
# •	On the first line:
# o	If the traveller has less than or equal to 0 health:
# "Player is dead. Maze over!"
# o	If the traveller survived with more than 0 health and managed to escape the maze:
# "Player escaped the maze. Danger passed!"
# •	On the second line, print the final value of the traveller's health following the
# format:
# "Player's health: {health value} units"
# •	On the next lines, print the final state of the matrix with the traveller in its
# ending position. Each row - on a new line.
# Constraints
# •	The commands are guaranteed to lead him either to escape out of the maze or to die by
# monsters, ensuring that the commands are sufficient in all cases.
# •	Some commands may lead our hero outside of the boundaries of the matrix. Do not allow
# that.
# •	The size of the matrix will always be a valid positive integer in the range [4,10].
# •	The last known position of the traveller should always be marked with 'P' in the final
# state of the matrix.

n = int(input())
health = 100
maze = []
p_row, p_col = 0, 0

for row in range(n):
    maze.append([char for char in input()])

    for col in range(n):
        if maze[row][col] == 'P':
            p_row = row
            p_col = col

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
command = input()
end_reached = False

while True:
    r, c = p_row + directions[command][0], p_col + directions[command][1]

    if r >= n or r < 0 or c >= n or c < 0:
        command = input()
        continue
    else:
        if maze[r][c] == 'M':
            health -= 40
        elif maze[r][c] == 'H':
            health += 15
        elif maze[r][c] == 'X':
            end_reached = True

    if health <= 0:
        health = 0
    elif health > 100:
        health = 100

    maze[p_row][p_col] = '-'
    p_row = r
    p_col = c
    maze[p_row][p_col] = 'P'

    if end_reached or health == 0:
        break

    command = input()

if health <= 0:
    print('Player is dead. Maze over!')
else:
    print('Player escaped the maze. Danger passed!')

print(f"Player's health: {health} units")

for row in maze:
    print(''.join(char for char in row))
