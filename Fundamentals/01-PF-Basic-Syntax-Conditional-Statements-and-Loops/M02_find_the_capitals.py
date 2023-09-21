# Write a program that takes a single string and prints a list of all the capital letters indices.

input_line = input()

list_capitals = []

for i in range(0, len(input_line)):
    if ord(input_line[i]) in range(65, 91):
        list_capitals.append(i)

print(list_capitals)