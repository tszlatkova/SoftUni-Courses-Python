# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until
# the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence,
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements.
# •	On the following lines, you will receive integers until the command "end".
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console
# the following message:
# "Congrats! You have found matching elements - {element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console
# the following message:
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following
# message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.

input_line = input().split(' ')

move = input()
moves_count = 0
won = False

while move != 'end':
    move_list = [int(i) for i in move.split(' ')]
    move_list = sorted(move_list)
    moves_count += 1

    if move_list[0] == move_list[1] or move_list[0] >= len(input_line) or move_list[0] < 0\
            or move_list[1] >= len(input_line) or move_list[1] < 0:
        add_elements = [f'-{moves_count}a', f'-{moves_count}a']
        midpoint = len(input_line) // 2
        input_line = input_line[0:midpoint] + add_elements + input_line[midpoint:]
        print('Invalid input! Adding additional elements to the board')
        move = input()
        continue

    if input_line[move_list[0]] == input_line[move_list[1]]:
        pop_element = input_line.pop(move_list[0])
        input_line.pop(move_list[1]-1)
        print(f'Congrats! You have found matching elements - {pop_element}!')
    else:
        print('Try again!')

    if len(input_line) == 0:
        print(f'You have won in {moves_count} turns!')
        won = True
        break

    move = input()

if not won:
    print(f'Sorry you lose :(')
    print(*input_line)
