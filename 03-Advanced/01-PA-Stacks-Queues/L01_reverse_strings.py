# Write a program that:
#
# · Reads an input string
#
# · Reverses it using a stack
#
# · Prints the result back on the console

input_string = input()

list_input_string = []
reversed_string = ''

for i in range(len(input_string)):
    list_input_string.append(input_string[i])

for _ in range(len(list_input_string)):
    reversed_string += list_input_string.pop()

print(reversed_string)
