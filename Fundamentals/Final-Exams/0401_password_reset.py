# Yet again, you have forgotten your password. Naturally, it's not the first time this has happened. Actually, you
# got so tired of it that you decided to help yourself with an intelligent solution.
# Write a password reset program that performs a series of commands upon a predefined string. First, you will receive
# a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a
# single space. The commands will be the following:
# •	"TakeOdd"
# o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# •	"Cut {index} {length}"
# o	Gets the substring with the given length starting from the given index from the password and removes its first
# occurrence, then prints the password on the console.
# o	The given index and the length will always be valid.
# •	"Substitute {substring} {substitute}"
# o	If the raw password contains the given substring, replace all of its occurrences with the substitute text given
# and print the result.
# o	If it doesn't, prints "Nothing to replace!".

# Input
# •	You will be receiving strings until the "Done" command is given.

# Output
# •	After the "Done" command is received, print:
# o	"Your password is: {password}"
# Constraints
# •	The indexes from the "Cut {index} {length}" command will always be valid.

def odd_indices(password):
    new_password = ''
    for i in range(len(password)):
        if i % 2 != 0:
            new_password += password[i]

    return new_password


def cutting_substring(password, index, length):
    substring = password[index:index + length]
    password = password.replace(substring, '', 1)

    return password


def substitute(password, substring, substitute):
    password = password.replace(substring, substitute)

    return password


password = input()

while True:
    command = input()

    if command == 'Done':
        break

    command = command.split(' ')
    action = command[0]

    if action == 'TakeOdd':
        password = odd_indices(password)
        print(password)
    elif action == 'Cut':
        idx, length = int(command[1]), int(command[2])
        password = cutting_substring(password, idx, length)
        print(password)
    elif action == 'Substitute':
        substring, subst = command[1], command[2]

        if substring in password:
            password = substitute(password, substring, subst)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')
