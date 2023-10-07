# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def valid_password(key: str):
    valid = True

    if len(key) not in range(6,11):
        valid = False
        print(f'Password must be between 6 and 10 characters')

    count_digits = 0
    only_digits_letters = True

    for i in range(len(key)):
        if ord(key[i]) in range(48, 58):
            count_digits += 1
        elif ord(key[i]) in range(65, 91) or ord(key[i]) in range(97, 123):
            continue
        else:
            valid = False
            only_digits_letters = False

    if not only_digits_letters:
        print(f'Password must consist only of letters and digits')

    if count_digits < 2:
        valid = False
        print(f'Password must have at least 2 digits')

    return valid


input_password = input()

if valid_password(input_password):
    print(f'Password is valid')
    