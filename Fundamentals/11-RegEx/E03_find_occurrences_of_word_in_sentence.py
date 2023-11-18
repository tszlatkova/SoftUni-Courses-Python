# Write a program that finds how many times a word is used in a string. The output is a single number indicating the
# number of times the string contains the word. Note that letter case does not matter – it is case-insensitive.

import re

sentence = input()
key_word = input()

pattern = fr'\b{key_word}\b'

count_word = len(re.findall(pattern, sentence, re.IGNORECASE))

print(count_word)
