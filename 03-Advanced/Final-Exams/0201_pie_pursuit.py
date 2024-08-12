# You will receive two sequences on two separate lines. Each sequence will consist of
# integer values,
# separated by a single whitespace.
# The first sequence represents contestants, each value indicating the total count of
# pieces of pie a contestant can consume, while the second sequence represents the pies,
# signifying the number of pieces each pie contains.
# Contest Rules
# •	The competition continues until no more pies are left or no more contestants remain
# in the battle
# •	The contest kicks off with the first contestant facing the last pie in the sequence
# •	If the contestant's pie-eating capacity is greater than or equal to the pie's size,
# they manage to eat the entire pie, subtracting the pie's value (count of pie pieces)
# from the contestant's value
# (pie-eating capacity). The pie is removed from the collection.
# o	If the contestant's pie-eating capacity reaches 0, bid them farewell from the contest
# (remove the contestant from the competition).
# o	Otherwise, move the satisfied contestant to the back of the lineup, with the remaining
# pie-eating capacity.
# •	If the pie's size exceeds the contestant's pie-eating capacity, the contestant
# consumes as many pieces as possible, subtracting the eaten pieces (contestant's
# capacity), from the pie's size.
# o	The pie remains in the sequence with the value of pieces left.
# o	If the pie's size reaches 1 piece, remove the pie, adding the remaining piece to the
# next pie in the sequence.
# o	If this is the last pie, be careful, you won’t be able to add a piece to the next pie.
# Just leave that last piece back in the sequence.
# o	Say goodbye to the contented contestant from the contest (remove the contestant from
# the competition).
# •	In the end:
# o	If the pies are over, and there are contestants left, print on the console:
# "We will have to wait for more pies to be baked!" and the final state of the
# contestants' sequence on a separate line.
# o	If both the pies and contestants are over, it means that we have a champion. Print on
# the console: "We have a champion!"
# o	If the contestants are over, but there are pies left, print on the console:
# "Our contestants need to rest!" and the final state of the pie sequence on a separate
# line.
# Let the Pie Pursuit unfold and discover who will be the ultimate champion!

# Input / Constraints
# •	On the first line, you will receive the integers, representing the contestant's
# pie-eating capacity, separated by a single space.
# •	On the second line, you will receive the integers, representing the number of pieces
# each pie contains, separated by a single space.

# Output
# The following result should be printed on the Console, on separate lines:
# •	If the pies are over, and there are contestants left:
# o	"We will have to wait for more pies to be baked!"
# o	The final state of the contestants' sequence:
# "Contestants left: {contestant1}, {contestant2}, … {contestantn}"
# •	If both the pies and contestants are over:
# o	"We have a champion!"
# •	If the contestants are over, but there are pies left:
# o	"Our contestants need to rest!"
# o	The final state of the pie sequence
# o	"Pies left: {pie1}, {pie2}, … {pien}"

from collections import deque

contestants = deque(int(x) for x in input().split(' '))
pies = [int(x) for x in input().split(' ')]

while True:
    if not pies or not contestants:
        break

    current_cont = contestants.popleft()
    current_pie = pies.pop()

    if current_cont >= current_pie:
        current_cont -= current_pie

        if current_cont > 0:
            contestants.append(current_cont)
    else:
        current_pie -= current_cont

        if current_pie == 1 and len(pies) > 0:
            pies[0] += current_pie
        else:
            pies.append(current_pie)


if not pies:
    if not contestants:
        print('We have a champion!')
    else:
        print('We will have to wait for more pies to be baked!')
        print(f"Contestants left: {' '.join(str(x) for x in contestants)}")
else:
    print('Our contestants need to rest!')
    print(f"Pies left: {', '.join(str(x) for x in sorted(pies))}")
