# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

input_list = input().split(' ')

output_list = []

for i in range(len(input_list)):
    output_list.append(round(float(input_list[i])))

print(output_list)