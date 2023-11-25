# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  The cool
# threshold could be a huge number, so be mindful.
# An emoji is valid when:
# •	It is surrounded by 2 characters, either "::" or "**"
# •	It is at least 3 characters long (without the surrounding symbols)
# •	It starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined
# by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that take all emojis out of the text, count them and
# print only the cool ones on the console.
# Input
# •	On the single input, you will receive a piece of string.
# Output
# •	On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
# •	On the following line, print the count of all emojis found in the text in the format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"
# Constraints
# There will always be at least one digit in the text!

import re


def cool_threshold(text):
    total_coolness = 1
    for character in text:
        if character.isdigit():
            total_coolness *= int(character)

    return total_coolness


def emoji_coolness(text_emoji):
    coolness = 0
    for letter in text_emoji:
        coolness += ord(letter)

    return coolness


input_text = input()

pattern = r'(:|\*){2}([A-Z][a-z]{2,})\1{2}'

emojis = re.findall(pattern, input_text)

text_coolness = cool_threshold(input_text)

print(f'Cool threshold: {text_coolness}')

print(f'{len(emojis)} emojis found in the text. The cool ones are:')

for i in range(len(emojis)):
    current_emoji = emojis[i][1]
    surrounding = emojis[i][0] * 2
    if emoji_coolness(current_emoji) > text_coolness:
        print(surrounding + current_emoji + surrounding)
