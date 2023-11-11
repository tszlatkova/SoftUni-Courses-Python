# Write a program that receives a text and a string of banned words, separated by a comma and space ", ". All banned
# words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.

banned_words = input().split(', ')
text = input()

for word in banned_words:
    while word in text:
        word_to_replace_with = '*' * len(word)
        text = text.replace(word, word_to_replace_with)

print(text)