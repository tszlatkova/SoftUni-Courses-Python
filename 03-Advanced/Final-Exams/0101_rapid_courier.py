# On the first line, you will be given a sequence of integers representing packages that
# need to be delivered, with the values of their weight.
# On the next line, you will be given another sequence of integers representing couriers
# with their loading capacities.
# Until there are packages to deliver and couriers available, the program continues
# running.
# Track the total weight of packages delivered by your couriers.
# You need to compare the last package to the first courier:
# •	If the courier can deliver the package (the capacity of the courier is equal to or
# greater than the weight of the package), he does the delivery:
# o	If the capacity of the courier is greater than the weight of the package, reduce the
# courier's capacity by twice the package's weight:
# 	If the new courier's capacity is positive, the courier moves at the back of the
# sequence with the updated capacity.
# 	If the new capacity is zero or negative, remove the courier.
# o	Аdd the weight of the package to the total delivered weight.
# o	Remove the package from the sequence.
# •	If the courier cannot deliver the package (the capacity of the courier is less than
# the weight of the package), subtract the courier's capacity from the package's weight
# o	Return the remaining weight to the sequence (on its initial position), and remove
# the courier.
# o	Add the delivered portion of the package's weight to the total delivered weight.

# Input / Constraints

# •	On the first line, you will receive integers representing the weight of the packages
# to be delivered, separated by a single space.
# •	On the second line, you will receive integers representing the capacities of the
# couriers, separated by a single space.
# •	All given numbers will be valid integers in the range [0; 100].

# Output

# The output of your program should be printed on the Console, on separate lines,
# formatted according to the following rules:
# •	At the end of the program, print the weight of the packages delivered:
# o	"Total weight: {total_weight} kg"
# •	If all of the packages are delivered and there are no couriers left:
# o	"Congratulations, all packages were delivered successfully by the couriers today."
# •	If there are packages left but no more couriers available:
# o	"Unfortunately, there are no more available couriers to deliver the following
# packages: {package1}, {package2}, (…),{packagen}"
# o	Print the packages in their current order
# •	If there are couriers left but there are no more packages to deliver:
# o	"Couriers are still on duty: {couriers1}, {couriers2}, (…),{couriersn} but there are
# no more packages to deliver."
# o	Print the couriers in their current order

from collections import deque

packages = [int(x) for x in input().split(' ')]
couriers = deque(int(x) for x in input().split(' '))
total_delivered_weight = 0

while True:
    if len(packages) == 0 or len(couriers) == 0:
        break

    current_package = packages.pop()
    current_courier = couriers.popleft()

    if current_courier >= current_package:
        current_courier -= current_package * 2

        if current_courier > 0:
            couriers.append(current_courier)

        total_delivered_weight += current_package
    else:
        current_package -= current_courier
        packages.append(current_package)
        total_delivered_weight += current_courier

print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print('Congratulations, all packages were delivered successfully by the couriers '
          'today.')
elif not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the "
          f"following packages: {', '.join(str(x) for x in packages)}")
elif not packages:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} "
          f"but there are no more packages to deliver.")

# Input 1
# 
# 2 4 6 8
# 8 6 4 2
#
# Output 1
#
# Total weight: 20 kg
# Congratulations, all packages were delivered successfully by the couriers today.
#
#
# Input 2
#
# 13 11 5
# 5 11
#
# Output 2
#
# Total weight: 16 kg
# Unfortunately, there are no more available couriers to deliver the following
# packages: 13
#
#
# Input 3
#
# 3 7 14
# 2 2 2 1 7
#
# Output 3
#
# Total weight: 14 kg
# Unfortunately, there are no more available couriers to deliver the following
# packages: 3, 7


