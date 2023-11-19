# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on
# separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def valid_username(username: str):
    if valid_length(username) and valid_characters(username) and no_redundant_symbols(username):
        return True

    return False


def valid_length(username: str):
    if 3 <= len(username) <= 16:
        return True

    return False


def valid_characters(username: str):
    for symbol in username:
        if not (symbol.isalpha() or symbol.isdigit() or symbol in ['-', '_']):
            return False

    return True


def no_redundant_symbols(username: str):
    if ' ' in username:
        return False

    return True


usernames = input().split(', ')

for user in usernames:
    if valid_username(user):
        print(user)
