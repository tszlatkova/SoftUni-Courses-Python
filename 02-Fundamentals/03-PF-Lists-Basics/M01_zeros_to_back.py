# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
# and moves them to the back without messing up the other elements. Print the resulting integer list.

input_line = input().split(', ')

only_zeros = []
not_zeros = []

for i in range(len(input_line)):
    number = int(input_line[i])

    if number == 0:
        only_zeros.append(number)
    else:
        not_zeros.append(number)

print(not_zeros + only_zeros)