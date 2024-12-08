# Create a generator function called get_primes() which should receive a list of integer
# numbers and return a list containing only the prime numbers from the initial list.
# You can learn more about prime numbers here:

from typing import List
from math import sqrt


def get_primes(ls: List[int]):
    for number in ls:
        if number < 2:
            continue
        for i in range(2, int(sqrt(number))+1):
            if number % i == 0:
                break
        else:
            yield number


print('Test code 1')
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print('Test code 2')
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
