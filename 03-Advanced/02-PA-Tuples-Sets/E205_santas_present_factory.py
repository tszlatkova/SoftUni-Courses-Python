# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400
#
# You should take the last box with materials and the first magic level value to craft a
# toy. Their multiplication calculates the total magic level. If the result equals one of
# the levels described in the table above, you craft the present and remove both materials
# and magic value. Otherwise:
# •	If the product of the operation is a negative number, you should sum the values
# together, remove them both from their positions, and add the result to the materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive
# number, remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting
# the presents.
# Stop crafting presents when you run out of boxes of materials or magic-level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle

# Input
# •	The first line of input will represent the values of boxes with materials - integers,
# separated by a single space
# •	On the second line, you will be given the magic values - integers again, separated by
# a single space

# Output
# •	On the first line - print whether you've succeeded in crafting the presents:
# o	"The presents are crafted! Merry Christmas!"
# o	"No presents this Christmas!"
# •	On the next two lines print the materials and magic that are left, if there are any
# (otherwise skip the line)
# o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
# o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
# •	On the next lines print the presents you have crafted, ordered alphabetically in the
# format:
# o	"{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"

# Constraints
# •	All the materials' values will be integers in the range [-100, 100]
# •	Magic level values will be integers in the range [-100, 100]
# •	In all cases, at least one present will be crafted

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

toys = {'Doll': [150,0], 'Wooden train': [250,0],
        'Teddy bear': [300,0], 'Bicycle': [400,0]}
# the first integer in the list is the required magic, and the second - the quantity

created_toy = False
christmas = False

while materials and magic:

    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue
    else:
        total_magic = materials[-1] * magic[0]

        if total_magic > 0:
            for key in toys.keys():
                if toys[key][0] == total_magic:
                    toys[key][1] += 1
                    materials.pop(), magic.popleft()
                    created_toy = True
                    break

            if created_toy:
                created_toy = False
                if (toys['Doll'][1] == 1 and toys['Wooden train'][1] == 1) or \
                        (toys['Teddy bear'][1] == 1 and toys['Bicycle'][1] == 1):
                    christmas = True
            else:
                magic.popleft()
                materials[-1] += 15
        else:
            sum_to_add = materials.pop() + magic.popleft()
            materials.append(sum_to_add)

print("The presents are crafted! Merry Christmas!" if christmas
      else "No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key in sorted(toys.keys()):
    amount = toys[key][1]
    if amount > 0:
        print(f"{key}: {amount}")
