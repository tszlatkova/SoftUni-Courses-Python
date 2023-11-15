# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each
# character with the corresponding character three positions forward in the ASCII table. For example, A would be
# replaced with D, B would become E, and so on. Print the encrypted text.

massage_to_encrypt = input()

caesar_cipher = ''

for symbol in massage_to_encrypt:
    caesar_cipher += chr(ord(symbol) + 3)

print(caesar_cipher)