# Create a generator function called possible_permutations() which should receive a list
# and return lists with all possible permutations between its elements.

from itertools import permutations
from typing import List


def possible_permutations(ls: List):

    for perm in permutations(ls):
        yield list(perm)


print('Test code 1')
[print(n) for n in possible_permutations([1, 2, 3])]
print('\nTest code 2')
[print(n) for n in possible_permutations([1])]
