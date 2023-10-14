# You will be receiving to-do notes until you get the command "End". The notes will be in the format:
# "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# •	Use the pop() and insert() methods.

def sort_priorities(to_do_list: list):
    sorted_to_do = []

    for i in range(1, 11):
        for j in range(len(to_do_list)):
            if i == to_do_list[j][0]:
                sorted_to_do.append(to_do_list[j][1])

    return sorted_to_do


input_line = input()

to_do = []

while input_line != 'End':
    input_line = input_line.split('-')
    input_line[0] = int(input_line[0])

    to_do.append(input_line)

    input_line = input()

print(sort_priorities(to_do))