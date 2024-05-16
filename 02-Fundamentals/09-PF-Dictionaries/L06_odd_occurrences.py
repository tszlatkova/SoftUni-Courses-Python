# Write a program that prints all elements from a given sequence of words that occur an odd number of times
# (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.

words = input().split(' ')

words_count = {}

for word in words:
    word_lower = word.lower()

    if word.lower() not in words_count:
        words_count[word_lower] = 1
    else:
        words_count[word_lower] += 1

words_odd_occurrence = [key for (key, value) in words_count.items() if value % 2 != 0]

print(' '.join(words_odd_occurrence))
