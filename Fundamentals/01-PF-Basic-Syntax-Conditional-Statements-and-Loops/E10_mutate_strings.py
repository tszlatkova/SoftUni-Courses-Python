# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()

if len(first_string) == len(second_string):
    first_string_list = list(first_string)
    for letter in range(0, len(second_string)):
        if first_string_list[letter] != second_string[letter]:
            first_string_list[letter] = second_string[letter]
            print("".join(first_string_list))
