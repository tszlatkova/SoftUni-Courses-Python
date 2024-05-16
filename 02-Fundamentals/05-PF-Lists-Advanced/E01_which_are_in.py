# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the
# first input line, which are substrings of any string in the second input line.

seq1 = input().split(', ')
seq2 = input().split(', ')

subset = []

for word1 in seq1:
    for word2 in seq2:
        if word1 in word2:
            subset.append(word1)
            break

print(subset)