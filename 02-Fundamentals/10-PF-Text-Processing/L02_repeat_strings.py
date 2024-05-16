# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times,
# where N is the length of the string. Print the final strings concatenated into one string.

input_line = input().split()

concatenated_strings = ''

for word in input_line:
    concatenated_strings += word * len(word)

print(concatenated_strings)
