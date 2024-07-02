# You will be given numbers separated by a space. Write a program that prints the number
# of occurrences of each number in the format "{number} - {count} times". The number must
# be formatted to the first decimal point.

numbers = tuple([float(num) for num in input().split()])

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = numbers.count(num)

for key, value in occurrences.items():
    print(f"{key:.1f} - {value} times")
