# On the first line, you will be given a sequence containing integers representing bee
# groups that live in a beehive.
# On the second line, you will be given another sequence of integers representing
# bee-eaters groups living near the beehive.
# Bees and bee-eaters are eternal enemies and are always fighting. Bees are known as the
# defenders of their hive while the bee-eaters are known as the attackers.
# Until there are bees and bee-eaters available, the program will continue running.
# You need to compare the first group of bees to the last group of bee-eaters (See the
# Examples):
# •	They start a fight until at least one of the groups is defeated.
# One bee-eater can kill 7 (seven) bees at once, per each fight, then dies.
# If one attacker needs to fight fewer defenders in number (less than 7), it survives
# while the defenders are considered defeated. In the next battle, it can kill 7 (seven)
# defenders again.
# o	If the bee-eaters from the current fighting group win (there are 0 (zero) remaining
# bees in the corresponding group) return the survived bee-eaters to the sequence
# (in their initial position). The defeated bee group is removed.
# o	If the bees from the current fighting group win, (there are 0 (zero) remaining
# bee-eaters of the corresponding group) add the bees that survived to the back of the
# bees collection. The defeated group of bee-eaters is removed.
# o	If the result is a draw, remove both groups from their collections and proceed to the
# next ones.

# Input / Constraints
# •	On the first line, you will receive integers representing the bee groups, separated
# by a single space. (See the Examples)
# •	On the second line, you will receive integers representing the bee-eaters groups,
# separated by a single space. (See the Examples)
# •	The given numbers will be valid positive integers in the range [1 - 100] inclusive.

# Output
# The output of your program should be printed on the Console, on separate lines,
# depending on the following outcome variations:
# •	On the first line:
# "The final battle is over!"
# •	On the second line:
# o	If bees and bee-eaters have slaughtered each other, print:
# "But no one made it out alive!"
# o	If there are bees that survived, print:
# "Bee groups left: {bee_group1, bee_group2, …, bee_groupN}"
# 	Print the bee groups in their current order, separated by comma and space ", ".
# o	If there are bee-eater groups that have survived, print:
# "Bee-eater groups left: {bee_eaters_group1, …, bee_eaters_groupN}"
# 	Print the bee-eater groups in their current order, separated by comma and space ", ".

from collections import deque

bees = deque([int(x) for x in input().split(' ')])
bee_eaters = [int(x) for x in input().split(' ')]

while len(bees) > 0 and len(bee_eaters) > 0:
    current_defenders = bees.popleft()
    current_attackers = bee_eaters.pop()

    count = current_attackers
    for _ in range(current_attackers):
        if current_defenders >= 7:
            count -= 1
            current_defenders -= 7
        elif current_defenders < 7:
            current_defenders = 0
            break

        if count == 0:
            break

    if count > 0 and current_defenders == 0:
        bee_eaters.append(count)
    elif count == 0 and current_defenders > 0:
        bees.append(current_defenders)

print('The final battle is over!')

if not bees and not bee_eaters:
    print('But no one made it out alive!')
elif not bee_eaters:
    print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif not bees:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")

# Input 1
#
# 29 41 9
# 1 6
#
# Output 1
#
# The final battle is over!
# Bee groups left: 27, 2

# Input 2
#
# 14 6
# 1 3 2
#
# Output 2
#
# The final battle is over!
# Bee-eater groups left: 1, 3
