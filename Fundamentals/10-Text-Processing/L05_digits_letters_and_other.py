# Write a program that receives a single string. On the first line, print all the digits found in the string,
# on the second – all the letters, and on the third – all the other characters. There will always be at least one digit,
# one letter, and one other character.

input_string = input()

digits, letters, others = '', '', ''

for character in input_string:
    if ord(character) in range(97, 123) or ord(character) in range(65, 91):  # if char.isalpha()
        letters += character
    elif ord(character) in range(48, 58):  # if char.isdigit()
        digits += character
    else:
        others += character

print(f'{digits}\n{letters}\n{others}')
