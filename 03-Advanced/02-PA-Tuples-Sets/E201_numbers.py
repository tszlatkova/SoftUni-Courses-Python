# First, you will be given two sequences of integer values on different lines. The values
# of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the following N lines, you will receive one of
# the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the
# first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the
# second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in
# the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in
# the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it
# is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values
# in each sequence should be sorted in ascending order.

first_set = set(int(x) for x in input().split())
second_set = set(int(y) for y in input().split())

for _ in range(int(input())):
    input_line = input().split()
    command = input_line[0] + ' ' + input_line[1]
    numbers = [int(x) for x in input_line[2:]]

    if command == 'Add First':
        first_set.update(numbers)
    elif command == 'Add Second':
        second_set.update(numbers)
    elif command == 'Remove First':
        first_set.difference_update(numbers)
    elif command == 'Remove Second':
        second_set.difference_update(numbers)
    elif command == 'Check Subset':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')

print(*sorted(list(first_set)), sep=', ')
print(*sorted(list(second_set)), sep=', ')
