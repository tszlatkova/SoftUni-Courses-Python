# Write a program that receives a single word, reverses it, and prints it.

word = str(input())
reverse = ''

for letter in range(len(word) - 1, -1, -1):
    reverse = reverse + word[letter]

print(reverse)