# SofUni solution

def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for cur_idx in range(idx + 1, len(nums)):
            if nums[cur_idx] < nums[min_idx]:
                min_idx = cur_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


numbers = [int(x) for x in input().split()]
selection_sort(numbers)
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
