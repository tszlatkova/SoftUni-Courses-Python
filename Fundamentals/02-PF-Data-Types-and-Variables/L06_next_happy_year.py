# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct
# digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.

current_year = int(input())

happy_year = False

while not happy_year:
    current_year += 1
    string_year = str(current_year)

    similar = False
    for i in range(0, len(string_year)):
        for j in range(i + 1, len(string_year)):
            if string_year[i] == string_year[j]:
                similar = True

    if not similar:
        happy_year = True

if happy_year:
    print(f'{current_year}')