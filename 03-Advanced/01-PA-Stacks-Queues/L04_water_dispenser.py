# Write a program that keeps track of people getting water from a dispenser and the amount
# of water left at the end.
#
# On the first line, you will receive the starting quantity of water (integer) in a
# dispenser. Then, on the following lines, you will be given the names of some people who
# want to get water (each on a separate line) until you receive the command "Start". Add
# those people to a queue. Finally, you will receive some commands until the command
# "End":
#
# - "{liters}" - litters (integer) that the current person in the queue wants to get.
# Check if there is enough water in the dispenser for that person.
#
# o If there is enough water, print "{person_name} got water" and remove him/her from
# the queue.
#
# o Otherwise, print "{person_name} must wait" and remove the person from the queue
# without reducing the water in the dispenser.
#
# - "refill {liters}" - add the given litters in the dispenser.
#
# In the end, print how many liters of water have left in the format: "{left_liters}
# liters left".

from collections import deque

quantity = int(input())
input_line = input()
names = deque([])

while input_line != 'Start':
    names.append(input_line)

    input_line = input()

command = input()

while command != 'End':
    command = command.split(' ')

    if command[0] == 'refill':
        quantity += int(command[1])
    else:
        requested_water = int(command[0])

        if requested_water <= quantity:
            quantity -= requested_water
            print(f'{names.popleft()} got water')
        else:
            print(f'{names.popleft()} must wait')

    command = input()

print(f'{quantity} liters left')
