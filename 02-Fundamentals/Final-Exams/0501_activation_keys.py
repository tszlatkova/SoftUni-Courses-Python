# You are about to make some good money, but first, you need to think of a way to verify who paid for your product and
# who didn't. You have decided to let people use the software for a free trial period and then require an activation
# key to continue using the product. Before you can cash out, the last step is to design a program that creates unique
# activation keys for each user. So, waste no more time and start typing!
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# •	"Contains>>>{substring}":
# o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
# o	Otherwise, prints: "Substring not found!"
# •	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
# o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints
# the activation key.
# o	All given indexes will be valid.
# •	"Slice>>>{startIndex}>>>{endIndex}":
# o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
# o	Both indices will be valid.

# Input
# •	The first line of the input will be a string consisting of letters and numbers only.
# •	After the first line, until the "Generate" command is given, you will be receiving strings.

# Output
# •	After the "Generate" command is received, print:
# o	"Your activation key is: {activation key}"


def key_contains(key_string, substring):
    if substring in key_string:
        return True
    else:
        return False


def flip_letters(key_string, upper_or_lower, start_idx, end_idx):
    string_up_to_start = key_string[:start_idx]
    string_to_modify = key_string[start_idx:end_idx]
    string_after_end = key_string[end_idx:]
    modified_string = ''

    if upper_or_lower == 'Upper':
        for character in string_to_modify:
            if character.isalpha() and character.islower():
                modified_string += character.upper()
            else:
                modified_string += character
    elif upper_or_lower == 'Lower':
        for character in string_to_modify:
            if character.isalpha() and character.isupper():
                modified_string += character.lower()
            else:
                modified_string += character

    final_string = string_up_to_start + modified_string + string_after_end

    return final_string


input_line = input()

while True:
    command = input()

    if command == 'Generate':
        break

    command = command.split('>>>')
    action = command[0]

    if action == 'Contains':
        substring = command[1]

        if key_contains(input_line, substring):
            print(f'{input_line} contains {substring}')
        else:
            print(f'Substring not found!')

    elif action == 'Flip':
        upper_lower = command[1]
        start = int(command[2])
        end = int(command[3])

        input_line = flip_letters(input_line, upper_lower, start, end)
        print(input_line)

    elif action == 'Slice':
        start = int(command[1])
        end = int(command[2])
        input_line = input_line[:start] + input_line[end:]
        print(input_line)

print(f'Your activation key is: {input_line}')
