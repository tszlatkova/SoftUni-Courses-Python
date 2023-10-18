# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

def decipher_first_letter(word):
    word_list = list(word)
    number = []
    letters = []

    for i in range(len(word_list)):
        if 48 <= ord(word[i]) <= 57:
            number.append(word[i])
        else:
            letters.append(word[i])

    letter = chr(int(''.join(number)))
    word = letter + ''.join(letters)

    return word


def change_letters(word):
    word_list = list(word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]

    return ''.join(word_list)


code = input().split(' ')

for i in range(len(code)):
    code[i] = change_letters(decipher_first_letter(code[i]))

print(*code)





