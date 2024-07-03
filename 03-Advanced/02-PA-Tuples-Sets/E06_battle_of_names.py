# You will receive a number N. On the following N lines, you will be receiving names. You
# should sum the ASCII values of each letter in the name and integer divide it by the
# number of the current row (starting from 1). Save the result to a set of either odd or
# even numbers, depending on if the resulting number is odd or even. After that, sum the
# values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by
# ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the
# different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the
# symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

number_names = int(input())
current_row = 1
odd_numbers = set()
even_numbers = set()

for _ in range(number_names):
    name = input()
    name_ascii = 0

    for char in name:
        name_ascii += ord(char)
        name_sum = name_ascii // current_row

    if name_sum % 2 == 0:
        even_numbers.add(name_sum)
    else:
        odd_numbers.add(name_sum)

    current_row += 1

odd_sum = sum(odd_numbers)
even_sum = sum(even_numbers)

if odd_sum == even_sum:
    print(*odd_numbers.union(even_numbers), sep=', ')
elif odd_sum > even_sum:
    print(*odd_numbers.difference(even_numbers), sep=', ')
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=', ')
