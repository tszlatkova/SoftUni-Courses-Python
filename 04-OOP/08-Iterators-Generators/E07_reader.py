# Create a generator function called read_next() which should receive a different number
# of arguments (all iterable). On each iteration, the function should return each element
# from each sequence.

from typing import Iterable


def read_next(*collections: Iterable):
    for collection in collections:
        # for el in collection:
        #     yield el
        yield from collection


print('Test code 1')
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print('\n\nTest code 2')
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
