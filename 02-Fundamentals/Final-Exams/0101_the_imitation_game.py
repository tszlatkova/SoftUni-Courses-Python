# During World War 2, you are a mathematician who joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is
# given, you will be receiving strings with instructions for different operations that need to be performed upon the
# concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text

# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .

# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

def move_letters(string_to_change: str, number_of_letters: int):
    """
    Moves the first n letters to the back of the string
    """
    new_string = string_to_change[number_of_letters:] + string_to_change[:number_of_letters]
    return new_string


def inset_value(string_to_change: str, index: int, value_to_insert):
    """
    Inserts the given value before the given index in the string
    """
    new_string = string_to_change[:index] + value_to_insert + string_to_change[index:]
    return new_string


def change_occurrences(string_to_change: str, substring: str, replacement: str):
    """
    Changes all occurrences of the given substring with the replacement text
    """
    new_string = string_to_change.replace(substring, replacement)
    return new_string


message = input()

command = input()

while command != 'Decode':
    command = command.split('|')
    action = command[0]

    if action == 'Move':
        message = move_letters(message, int(command[1]))
    elif action == 'Insert':
        idx = int(command[1])
        value = command[2]
        message = inset_value(message, idx, value)
    elif action == 'ChangeAll':
        string_to_replace = command[1]
        replacement = command[2]
        message = change_occurrences(message, string_to_replace, replacement)

    command = input()

print(f'The decrypted message is: {message}')
