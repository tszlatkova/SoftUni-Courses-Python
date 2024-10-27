# Not tested in Judge.

# Write a program that draws the figure below depending on n.

# 2
# **
# *
# #
# ##

# 5
# *****
# ****
# ***
# **
# *
# #
# ##
# ###
# ####
# #####

def stars(n):
    if n == 1:
        return '*'

    result = '*' * n

    return f'{result}\n' + stars(n-1)


def hashtags(n, count=1):
    if count == n:
        return '#' * n

    result = '#' * count

    return f'{result}\n' + hashtags(n, count + 1)


num = int(input())

# print(stars(num))
# print(hashtags(num))


# Function from SoftUni

def print_figure(n):
    if n <= 0:
        return

    print('*' * n)

    print_figure(n - 1)

    print('#' * n)


print_figure(num)
