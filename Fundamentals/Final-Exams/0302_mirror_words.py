# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s
# different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you
# are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden
# word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols).
# •	Made up of letters only.
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a
# match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
# •	You will recive a string.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.

import re


def mirror_words(word1, word2):
    """
    Check if the second word, spelled backward, is the same as the first word
    and vice versa (casing matters!)
    """
    word1_list = list(word1)
    word2_list = list(reversed(word2))
    mirror = True

    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            if word1_list[i] != word2_list[i]:
                return False

    return mirror


text_string = input()

pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'

result = re.findall(pattern, text_string)
mirror = []

if len(result) == 0:
    print('No word pairs found!')
else:
    print(f'{len(result)} word pairs found!')

for pair in result:
    first_word = pair[1]
    second_word = pair[3]
    if mirror_words(first_word, second_word):
        mirror.append(f'{first_word} <=> {second_word}')

if len(mirror) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror))
