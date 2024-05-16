# You will be given number n. After that, you'll receive different strings n times. Your task is to check
# if the given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".",
# or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"

number = int(input())

for _ in range(1, number + 1):
    word = input()
    pure = True

    for letter in range(0, len(word)):
        if word[letter] == ',' or word[letter] == '.' or word[letter] == '_':
            pure = False
            break

    if pure:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')