# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях съществува
# число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на
# останалите (по абсолютна стойност)

# Мое решение

# n = int(input())
#
# total_sum = 0
# numbers = []
#
# for _ in range(n):
#     number = int(input())
#     numbers.append(number)
#     total_sum += number
#
# numbers.sort()
#
# max_number = max(numbers)
# sum_without_max = sum(numbers) - max_number
#
# if sum_without_max == max_number:
#     print('Yes')
#     print(f'Sum = {max_number}')
# else:
#     diff = abs(max_number - sum_without_max)
#     print('No')
#     print(f'Diff = {diff}')

import sys

n = int(input())
total_sum = 0
max_number = -sys.maxsize

for _ in range(n):
    current_number = int(input())
    total_sum += current_number

    if current_number > max_number:
        max_number = current_number

if total_sum - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(total_sum - max_number)
    print('No')
    print(f'Diff = {diff}')