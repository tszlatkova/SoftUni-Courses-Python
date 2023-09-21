# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False). A number is special when the sum of its
# digits is 5, 7, or 11.

n = int(input())

for number in range(1, n + 1):
    number_str = str(number)

    sum_digits = 0
    for i in range(0, len(number_str)):
        sum_digits += int(number_str[i])

    if sum_digits in [5, 7, 11]:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')