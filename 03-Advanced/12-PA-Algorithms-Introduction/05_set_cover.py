# Solution from SoftUni. Not tested in Judge.

# Write a program that finds the smallest subset of sets, which contains all elements
# from a given sequence.
# In the Set Cover problem, we are given two sets - a set of sets (we'll call it sets)
# and a universe (a sequence). The sets contain all elements from the universe and no
# others, however, some elements are repeated. The task is to find the smallest subset of
# sets that contains all elements in the universe.

# Input
# •	On the first line, you will receive the universe.
# •	On the second line, you will receive the target number of sets.
# •	On the next lines, you will receive different sets of sets.

def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:

        # finds the set from the list of sets that covers the maximum number of remaining
        # elements in the universe. The key parameter uses the intersection of sets with
        # the universe to determine the size of the overlap.
        best_set = max(remaining_sets, key=lambda s: len(universe_set.intersection(s)))

        if not universe_set.intersection(best_set):
            break

        # appends the selected set (best_set) to the chosen_sets list
        chosen_sets.append(best_set)

        # removes the elements covered by the selected set from the remaining universe
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return None

    return chosen_sets  # The function returns the list of selected sets that cover the
                        # entire universe


universe = list(map(int, input().split(', ')))
n = int(input())
sets = []

for _ in range(n):
    set_elements = list(map(int, input().split(', ')))
    sets.append(set_elements)

result = set_cover(universe, sets)

if result is None:
    print('No solution exists')
else:
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f'\nSets to take ({len(result)}): ')
    for s in result:
        print("{", ", ".join(map(str, s)), "}")


# Input 1:
# 1, 2, 3, 4, 5
# 4
# 1
# 2, 4
# 5
# 3
#
#
# Input 2:
# 1, 2, 3, 4, 5
# 4
# 1, 2, 3, 4, 5
# 2, 3, 4, 5
# 5
# 3
#
#
# Input 3:
# 1, 3, 5, 7, 9, 11, 20, 30, 40
# 6
#
#
# Input 4:
# 20
# 1, 5, 20, 30
# 3, 7, 20, 30, 40
# 9, 30
# 11, 20, 30, 40
# 3, 7, 40
