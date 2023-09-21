# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

number_small_letters = int(input())

for i in range(97, 97 + number_small_letters):
    for j in range(97, 97 + number_small_letters):
        for k in range(97, 97 + number_small_letters):
            print(f'{chr(i)}{chr(j)}{chr(k)}')