#  За Лора думите притежават голяма сила. Тя те моли да измислиш алгоритъм, с който да откриеш коя е
#  "най-силната" дума. До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие
#  силата на всяка една, трябва да се намери сборът от ASCII стойностите на символите, от които се състои думата.
#  Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви), полученият
#  сбор трябва да се умножи по дължината на думата, в противен случай, да се раздели на дължината и да се закръгли до
#  най-близкото цяло число надолу.
# Вход
# До получаване на команда "End of words" се чете по един ред от конзолата:
# •	дума – текст
# Изход
# След приключване на програмата се печата на един ред думата с "най-голяма сила":
# •	"The most powerful word is {думата с най-голяма сила} - {силата на думата}"

from math import floor

input_line = input()
max_points = 0
most_powerful_word = ''

while input_line != 'End of words':
    word = input_line
    word_points = 0

    for letter in range(len(word)):
        word_points += ord(word[letter])

    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        word_points *= len(word)
    else:
        word_points = floor(word_points / len(word))

    if word_points > max_points:
        max_points = word_points
        most_powerful_word = word

    input_line = input()

print(f'The most powerful word is {most_powerful_word} - {max_points}')