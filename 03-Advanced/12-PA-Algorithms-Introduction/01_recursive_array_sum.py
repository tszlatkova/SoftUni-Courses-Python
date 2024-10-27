# Not tested in Judge

# Write a program that finds the sum of all elements in an integer array. Use recursion.
# Note: In practice, this recursion should not be used here (instead use an iterative
# solution), this is just an exercise.

def sum_recursion(numbers, idx=0):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + sum_recursion(numbers, idx + 1)


nums = [int(x) for x in input().split()]

print(sum_recursion(nums))
