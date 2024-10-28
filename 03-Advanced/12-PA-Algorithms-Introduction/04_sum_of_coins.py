# Solution given by SoftUni.

# Write a program that gathers a sum of money using the least possible number of coins.
# This is the range of possible coin values:

# •	{ 1, 2, 5, 10, 20, 50 }

# You will receive the desired sum. The goal is to reach the sum using as few coins as
# possible using a greedy approach. We'll assume that each coin value and the desired sum
# are integers.

# Input
# •	On the first line, you will receive the coins.
# •	On the next line, you will receive the target sum.

def choose_coins(coins, target_sum):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while target_sum != 0 and index < len(coins):
        count_coins = target_sum // coins[index]

        target_sum %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if target_sum != 0:
        return 'Error'
    else:
        result = f'Number of coins to take: {sum(used_coins.values())}\n'
        for value, count in used_coins.items():
            result += f'{count} coin(s) with value {value}\n'
        return result.strip()


coin_input = input()
coins = list(map(int, coin_input.split(', ')))

target_sum = int(input())

result = choose_coins(coins, target_sum)
print(result)

# Example 1
# 1, 2, 5, 10, 20, 50
# 923
#
# Example 2
# 1
# 42
#
# Exapmle 3 (Error)
# 3, 7
# 11
#
# Example 4
# 1, 2, 5
# 2031154123
#
# Example 5
# 1, 10, 9
# 27


# .strip () -> Remove spaces at the beginning and at the end of the string

# Example
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)

# Output: banana
