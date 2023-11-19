# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses strings
# and prints each pair on a separate line in the format "{word} = {reversed_word}".

while True:
    word = input()

    if word.lower() == 'end':
        break
    else:
        print(f'{word} = {word[::-1]}')
