# On the first line, you will receive words separated by a single space. On the second line, you will receive a
# palindrome. First, you should print a list containing all the found palindromes in the sequence. Then, you should
# print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

def palindrome(word):
    backward_word = ''

    for letter in range(len(word) - 1, -1, -1):
        backward_word += word[letter]

    return word == backward_word


words = input().split(' ')
palindrome_to_search = input()

found_palindroms = []

for i in range(len(words)):
    if palindrome(words[i]):
        found_palindroms.append(words[i])

count_searched_palindrome = found_palindroms.count(palindrome_to_search)

print(found_palindroms)
print(f'Found palindrome {count_searched_palindrome} times')