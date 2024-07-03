# Write a program that reads a text from the console and counts the occurrences of each
# character in it. Print the results in alphabetical (lexicographical) order.

text = input()

characters_set = set()

for char in text:
    characters_set.add(char)

ordered_list = sorted(list(characters_set))
characters_occurrences = {}

for char in ordered_list:
    characters_occurrences[char] = text.count(char)

for key, value in characters_occurrences.items():
    print(f'{key}: {value} time/s')
