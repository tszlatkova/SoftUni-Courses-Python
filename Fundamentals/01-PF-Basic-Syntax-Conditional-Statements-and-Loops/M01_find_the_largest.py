# You will be given a number. Print the largest number that can be formed from the digits of the given number.

input_line = input()

list_numbers = []

for i in range(0, len(input_line)):
    list_numbers.append(int(input_line[i]))

list_sorted = sorted(list_numbers)

largest_number = ''
for i in range(len(input_line) - 1, -1, -1):
    largest_number += str(list_sorted[i])

print(int(largest_number))