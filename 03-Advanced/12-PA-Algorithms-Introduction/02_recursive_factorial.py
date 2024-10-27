# Not tested in Judge.

# Write a program that calculates the recursively factorial of a given number.
# NOTE: In practice, this recursion should not be used here (instead use an iterative
# solution).

# Hints
# Write a recursive method. It will take as arguments an integer number.
# •	The method should return the current element * the result of calculating the
# factorial of the current
# element - 1 (obtained by recursively calling it).
# •	The recursion should stop when the last element is reached

def fact_rec(num: int):
    if num == 0:
        return 1

    return num * fact_rec(num - 1)


n = int(input())

print(fact_rec(n))
