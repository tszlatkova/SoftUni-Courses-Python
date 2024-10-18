# Write a function named "accommodate" that receives information about guests waiting for
# accommodation and the available rooms.
# The function will receive an unknown number of arguments and keyword arguments:
# •	The arguments will be passed as follows:
# o	Guest groups as integers in the range [1-10] inclusive. (See the Examples)
# •	The keyword arguments will be passed as follows:
# o	Room number as a key - a unique string in the format "room_{number}".
# 	The number contains exactly 3 digits, in the range [100-999] inclusive.
# o	Room capacity as a value  - an integer in the range [1-6] inclusive.
# Example: room_101=5
# The program runs until all groups of guests have tried to complete the check-in process
# at the reception area.
# The receptionist tries to accommodate the groups of guests in their initial order,
# starting with the first group, and searches for the most suitable room.
# •	Best fit rule: A room is considered a best fit if it has a capacity equal to the
# number of guests. If there is no such room, choose the one with the smallest capacity
# that is greater than the guests' number. If multiple rooms have the same capacity, pick
# the one with the smallest room number.
# Hint: Order the available rooms by capacity ascending, then by room number ascending.
# •	Once a group is accommodated in a room, the room is no longer available.
# •	If no suitable room is found (the number of guests does not fit in any available
# room), the group remains unaccommodated.
# o	Keep track of the number of guests with unsuccessful accommodations.
# Once all guests have tried to complete the check-in process, the hotel software
# displays the result.
# •	If there are any successful accommodations, sort them by the room number ascending.
# •	Return the output as described below. (See the Output section)
# Note: Submit only the function in the judge system

# Input
# •	There will be no input from the console, just parameters passed to your function.

# Output
# •	If there are accommodations, return them sorted by room number and in the following
# format:
# "A total of {total_number_of_accommodations} accommodations were completed!
# <Room {room_number1} accommodates {guests1} guests>
# <Room {room_number2} accommodates {guests2} guests>
# …
# <Room {room_numberN} accommodates {guestsN} guests>"
# Note: If the room is "room_101" the number of the room is 101.
# •	Otherwise, return the message:
# "No accommodations were completed!"
# The output string should also contain information for the guests without accommodation
# and the empty hotel rooms if there are any:
# •	If there are guests without accommodation, return a message:
# "Guests with no accommodation: {total_number_of_unaccommodated_guests}"
# •	If there are empty rooms, return a message:
# "Empty rooms: {total_number_of_empty_rooms}"

# Constraints
# •	The arguments will always be integers in the range [1-10] inclusive.
# •	The keyword arguments will always have a key as a string in the format "room_{number}"
# and a value as an integer in the range [1-6] inclusive.
# •	The room numbers will be unique and contain exactly 3 digits in the range [100-999]
# inclusive.
# •	There will always be at least one argument and at least one keyword argument.

def accommodate(*args, **kwargs):
    all_guests = [int(x) for x in args]
    sorted_rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))
    accommodated_guests = {}
    not_accommodated_count = 0

    for group in all_guests:
        room_found = False
        for tup in sorted_rooms:
            if int(tup[1]) == group:
                accommodated_guests[tup[0]] = group
                room_found = True
                sorted_rooms.remove(tup)
                break

        if not room_found:
            for tup in sorted_rooms:
                if int(tup[1]) > group:
                    room_found = True
                    accommodated_guests[tup[0]] = group
                    sorted_rooms.remove(tup)
                    break

        if not room_found:
            not_accommodated_count += group

    result = ''

    if len(accommodated_guests) != 0:
        sorted_accommodated = sorted(accommodated_guests.items(),
                                     key=lambda x: x[0])
        result += f'A total of {len(accommodated_guests)} accommodations were completed!\n'
        for room in sorted_accommodated:
            result += f"<Room {room[0].split('_')[1]} accommodates {room[1]} guests>\n"
    else:
        result += 'No accommodations were completed!\n'

    if not_accommodated_count > 0:
        result += f'Guests with no accommodation: {not_accommodated_count}\n'

    if len(sorted_rooms) > 0:
        result += f'Empty rooms: {(len(sorted_rooms))}'

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

print(accommodate(10, 9, 8, room_307=6, room_802=5))

print(accommodate(1, 2, 4, 8, room_102=3, room_101=2, room_103=2))
