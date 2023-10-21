# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the
# first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will
# start receiving commands for manipulating the targets until the "End" command. The commands are the following:
# •	"Shoot {index} {power}"
# •	"Add {index} {value}"
# •	"Strike {index} {radius}"
# •	"End"
# o	Print the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"

# Input / Constraints
# •	On the first line, you will receive the sequence of targets – integer values [1-10000].
# •	On the following lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when the "Strike" command would empty the whole sequence.

# Output
# •	Print the appropriate message in case of any command if necessary.
# •	In the end, print the sequence of targets in the format described above.

def shoot(targets_list, index_list, power):
    """
    o Shoot the target at the index if it exists by reducing its value by the given power (integer value).
    o Remove the target if it is shot. A target is considered shot when its value reaches 0.
    """
    if 0 <= index_list < len(targets_list):
        targets_list[index_list] -= power

        if targets_list[index_list] <= 0:
            targets_list.pop(index_list)

    return targets_list


def add(targets_list, index_list, value):
    """
    o Insert a target with the received value at the received index if it exists.
    o If not, print: "Invalid placement!"
    """
    if 0 <= index_list < len(targets_list):
        targets_list.insert(index_list, value)
    else:
        print('Invalid placement!')

    return targets_list


def strike(targets_list, index_list, radius):
    """
    o Remove the target at the given index and the ones before and after it depending on the radius.
    o If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
    Example:  "Strike 2 2"
               {radius}	{radius} {strikeIndex} {radius}	{radius}
    """
    if 0 <= index_list < len(targets_list) and 0 <= index_list + radius < len(targets_list) and\
            0 <= index_list - radius < len(targets_list):
        for i in range(index_list + radius, index_list - radius - 1, -1):
            targets_list.pop(i)
    else:
        print('Strike missed!')

    return targets_list


targets = [int(i) for i in input().split(' ')]

command = input()

while command != 'End':
    command = command.split(' ')
    action = command[0]
    index = int(command[1])
    power_value_radius = int(command[2])

    if action == 'Shoot':
        targets = shoot(targets, index, power_value_radius)
    elif action == 'Add':
        targets = add(targets, index, power_value_radius)
    elif action == 'Strike':
        targets = strike(targets, index, power_value_radius)

    command = input()

print(*targets, sep = '|')