# SofUni's solution

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums


numbers = [int(x) for x in input().split()]
sort_nums = insertion_sort(numbers)
print(*sort_nums)


# Input 1:
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7
# 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18
# 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9
# 80 41 66 1 54 31 55 33 88 35 32 43
#
#
# Input 2:
# 5 4 3 2 1
