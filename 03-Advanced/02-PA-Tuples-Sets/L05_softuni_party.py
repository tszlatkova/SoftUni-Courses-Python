# There is a party at SoftUni. Many guests are invited, and there are two types of them:
# Regular and VIP. When a guest comes, check if they exist on any of the two reservation
# lists.
# On the first line, you will receive the number of guests – N. On the following N lines,
# you will be receiving their reservation codes. All reservation codes are 8 characters
# long, and all VIP numbers will start with a digit. Keep in mind that all reservation
# numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END"
# command.
# In the end, print the number of guests who did not come to the party and their
# reservation numbers:
# •	The VIP guests must be first.
# •	Both the VIP and the Regular guests must be sorted in ascending order.

number_guests = int(input())

vip = set()
regular = set()

for _ in range(number_guests):
    guest = input()

    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

coming_guest = input()

while coming_guest != 'END':

    if coming_guest[0].isdigit() and coming_guest in vip:
        vip.remove(coming_guest)
    elif coming_guest in regular:
        regular.remove(coming_guest)
    else:
        continue

    coming_guest = input()

all_guests = sorted(vip.union(regular))

print(len(all_guests))
print(*all_guests, sep='\n')

# Ines solution

# n = int(input())
#
# reservations = set()
#
# for _ in range(n):
#     guest_num = input()
#     reservations.add(guest_num)
#
# reservation_number = input()
#
# while reservation_number != "END":
#     if reservation_number in reservations:
#         reservations.remove(reservation_number)
#     reservation_number = input()
#
# print(len(reservations))
#
# sorted_reservations = sorted(reservations)
# for reservation in sorted_reservations:
#     print(reservation)
