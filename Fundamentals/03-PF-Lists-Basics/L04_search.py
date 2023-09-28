# On the first line, you will receive a number n. On the second line, you will receive a word. On the following
# n lines, you will be given some strings. You should add them to a list and print them. After that, you should
# filter out only the strings that include the given word and print that list too.

lines_number = int(input())
key_word = input()

words_list = []
filtered_list = []

for _ in range(lines_number):
    words_list.append(input())

print(words_list)

for string in words_list:
    if key_word in string:
        filtered_list.append(string)

print(filtered_list)

