# SoftUni Solution

# Implement an algorithm that finds the index of an element in a sorted array of integers
# in logarithmic time.

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left+right) // 2

        mid_el = numbers[mid_idx]
        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))


# Input 1:
# 1 2 3 4 5
# 1
#
#
# Input 2:
# -1 0 1 2 4
# 1
