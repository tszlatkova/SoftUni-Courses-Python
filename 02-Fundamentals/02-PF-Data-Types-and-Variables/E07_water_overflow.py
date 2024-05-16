# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines,
# which will follow. On the following n lines, you will receive liters of water (integers), which you should pour into
# your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the
# last line, print the liters in the tank.

lines_number = int(input())

tank_liters = 0

for i in range(1, lines_number + 1):
    water = int(input())

    if tank_liters + water > 255:
        print('Insufficient capacity!')
    else:
        tank_liters += water

print(tank_liters)