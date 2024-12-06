# Create a program that reads a positive integer N as input and prints on the console a
# rhombus with size n.

def top_part(num):
    result = ''
    for i in range(1, num+1):
        result += ' '*(num-i) + '*' + ' *'*(i-1)+'\n'

    return result


def bottom_part(num):
    result = ''
    for i in range(num-1, 0, -1):
        result += ' '*(num-i) + '*' + ' *'*(i-1)+'\n'

    return result


def rhombus_of_stars(num):
    return top_part(num) + bottom_part(num)


n = int(input())
print(rhombus_of_stars(n))


# Ines' solution

# n = int(input())
#
#
# def print_row(size, row):
#     print(f'{" " * (size - row)}{"* "* row}')
#
#
# def print_upper_part(size):
#     for row in range(1, size+1):
#         print_row(size, row)
#
#
# def print_bottom_part(size):
#     for row in range(size - 1, 0, -1):
#         print_row(size, row)
#
#
# def print_rhombus(size):
#     print_upper_part(size)
#     print_bottom_part(size)
#
#
# print_rhombus(n)
