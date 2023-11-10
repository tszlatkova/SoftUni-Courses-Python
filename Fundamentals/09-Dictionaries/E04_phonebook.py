# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already
# exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}". In case the contact isn't found, print:
# "Contact {name} does not exist."

contact = input().split('-')

phonebook = {}

while len(contact) == 2:
    name = contact[0]
    phone = contact[1]

    if name not in phonebook.keys():
        phonebook[name] = ''

    phonebook[name] = phone

    contact = input().split('-')

n = int(contact[0])

for _ in range(n):
    name = input()
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
