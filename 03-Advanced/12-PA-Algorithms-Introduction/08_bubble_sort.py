# SofUni's solution.

def bubble_sort(nums):
    is_sorted = False
    s = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - s):
            if nums[j-1] > nums[j]:
                is_sorted = False
                nums[j], nums[j-1] = nums[j-1], nums[j]

        s += 1


numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)


# Input 1:
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7
# 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18
# 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9
# 80 41 66 1 54 31 55 33 88 35 32 43
#
#
# Input 2:
# 5 4 3 2 1
