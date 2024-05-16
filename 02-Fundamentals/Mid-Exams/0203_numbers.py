# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value
# in the sequence, sorted in descending order.
# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated.
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# •	Print "No" if no numbers hold the above property.
# Constraints
# •	All input numbers are integers in the range [-1 000 000 … 1 000 000].
# •	The count of numbers is in the range [1…10 000].


def greater_than_average(list_numbers, average):
    list_of_numbers = []

    for number in sorted(list_numbers, reverse = True):
        if number > average:
            list_of_numbers.append(number)

        if len(list_of_numbers) == 5:
            break

    return list_of_numbers


numbers = [int(i) for i in input().split(' ')]

avg = sum(numbers) / len(numbers)

top_five_numbers = greater_than_average(numbers, avg)

if len(top_five_numbers) == 0:
    print(f'No')
else:
    print(*top_five_numbers)