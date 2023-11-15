# Write a program that reads a string from the console and replaces any sequence of the same letters with a single
# corresponding letter.

text = input()
not_repeating_chars = text[0]

for i in range(1, len(text)):
    if text[i] != text[i-1]:
        not_repeating_chars += text[i]

print(not_repeating_chars)