# The group of adventurists has gone on their first task. Now they should walk through fire - literally. They should
# use all the water they have left. Your task is to help them survive.
# Create a program that calculates the water needed to put out a "fire cell", based on the given information about
# its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the
# needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}# … {typeOfFire} = {valueOfCell}"
# Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each
# fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you should put it out by reducing the water with its value. Putting out fire also takes effort,
# and you need to calculate it. Its value is equal to 25% of the cell's value. In the end, you will have to print the
# total effort. Keep putting out cells until you run out of water. Skip it and try the next one if you do not have
# enough water to put out a given cell. In the end, print the cells you have put out in the following format:

# "Cells:
#  - {cell1}
#  - {cell2}
#  …
#  - {cellN}"
# "Effort: {effort}"
# The effort should be formatted to the second decimal place.
# In the end, print the total fire you have put out from all the cells in the following format:
# "Total Fire: {total_fire}"

# Input / Constraints
# •	On the 1st line, you will receive the fires with their cells in the format described above – integer numbers in
# the range [1…500].
# •	On the 2nd line, you will receive the water – an integer number in the range [0….100000].

# Output
# Print the output as described above.

input_line = input().split('#')
water = int(input())

fires = [input_line[i].split(' = ') for i in range(len(input_line))]
put_out_cells = []
effort = 0
total_fire = 0

for i in range(len(input_line)):

    if (fires[i][0] == 'High' and 81 <= int(fires[i][1]) <= 125 and int(fires[i][1]) <= water) \
            or (fires[i][0] == 'Medium' and 51 <= int(fires[i][1]) <= 80 and int(fires[i][1]) <= water)\
            or (fires[i][0] == 'Low' and 1 <= int(fires[i][1]) <= 50 and int(fires[i][1]) <= water):
        put_out_cells.append(int(fires[i][1]))
        effort += 0.25 * int(fires[i][1])
        total_fire += int(fires[i][1])
        water -= int(fires[i][1])

print('Cells:')

for cell in range(len(put_out_cells)):
    print(f'- {put_out_cells[cell]}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')