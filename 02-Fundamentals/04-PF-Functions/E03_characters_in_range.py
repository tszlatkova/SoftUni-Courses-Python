# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def characters_in_range(first_char, last_char):
    list_characters = []

    for i in range(first_char + 1, last_char):
        list_characters.append(chr(i))

    return list_characters


start = ord(input())
finish = ord(input())

print(*characters_in_range(start, finish))