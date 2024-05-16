# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything
# first. To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel",
# you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid.
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid.
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences).
# Note: After each command, print the current state of the string!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}".

# Input / Constraints
# •	JavaScript: you will receive a list of strings.
# •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.

# Output
# •	Print the proper output messages in the proper cases as described in the problem description.

def add_stop(stops, index, stop_to_add):
    stops_updated = stops[:index] + stop_to_add + stops[index:]

    return stops_updated


def remove_stop(stops, start_index, stop_index):
    stops_updated = stops[:start_index] + stops[stop_index + 1:]

    return stops_updated


def switch_stop(stops, old_stop, new_stop):
    stops = stops.replace(old_stop, new_stop)

    return stops


all_stops = input()

while True:
    command = input()

    if command == 'Travel':
        break

    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        idx = int(command[1])

        if idx < len(all_stops):
            string_to_add = command[2]
            all_stops = add_stop(all_stops, idx, string_to_add)

    elif action == 'Remove Stop':
        start_idx = int(command[1])
        end_idx = int(command[2])

        if start_idx <= end_idx < len(all_stops) and start_idx < len(all_stops):
            all_stops = remove_stop(all_stops, start_idx, end_idx)

    elif action == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in all_stops:
            all_stops = switch_stop(all_stops, old_string, new_string)

    print(all_stops)

print(f'Ready for world tour! Planned stops: {all_stops}')
