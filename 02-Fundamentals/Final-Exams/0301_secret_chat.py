# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go
# ahead and type it in!
# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is
# given, you will receive strings with instructions for different operations that need to be performed upon the
# concealed message to interpret it and reveal its actual content. There are several types of instructions, split by
# ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.

# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".

# Output
# •	After each set of instructions, print the resulting string.
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"


def insert_space(text: str, index_space):
    text = text[:index_space] + ' ' + text[index_space:]

    return text


def reverse_substring_once(text: str, substring_to_reverse):
    text = text.replace(substring_to_reverse, '', 1)
    reversed_substring = substring_to_reverse[::-1]
    text = text + reversed_substring

    return text


def replace_all_occurrences(text: str, substring, replacement):
    text = text.replace(substring, replacement)

    return text


secret_message = input()

while True:
    command = input()

    if command == 'Reveal':
        break

    command = command.split(':|:')
    action = command[0]

    if action == 'InsertSpace':
        idx = int(command[1])
        secret_message = insert_space(secret_message, idx)
        print(secret_message)
    elif action == 'Reverse':
        substring = command[1]
        if substring in secret_message:
            secret_message = reverse_substring_once(secret_message, substring)
            print(secret_message)
        else:
            print('error')
    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        secret_message = replace_all_occurrences(secret_message, substring, replacement)
        print(secret_message)

print(f'You have a new text message: {secret_message}')
