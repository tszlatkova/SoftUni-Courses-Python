# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

lines_number = int(input())

numbers_list = [int(input()) for _ in range(lines_number)]

command = input()
filtered_list = []

for number in numbers_list:
    if command == 'even' and number % 2 == 0:
        filtered_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        filtered_list.append(number)
    elif command == 'negative' and number < 0:
        filtered_list.append(number)
    elif command == 'positive' and number >= 0:
        filtered_list.append(number)

print(filtered_list)