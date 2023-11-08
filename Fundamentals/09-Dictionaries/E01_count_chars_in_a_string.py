# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

input_string = input()

chars_count = {}

for letter in input_string:

    if ord(letter) != 32:
        if letter not in chars_count:
            chars_count[letter] = 0

        chars_count[letter] += 1

for (key, value) in chars_count.items():
    print(f'{key} -> {value}')