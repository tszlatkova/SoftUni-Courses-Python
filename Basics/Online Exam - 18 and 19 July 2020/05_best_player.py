# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство.
# Информацията, която получавате ще бъде играч и колко гола е отбелязал. От вас се иска да отпечатате кой е играчът с
# най-много голове и дали е направил хет-трик. Хет-трик е, когато футболистът е вкарал 3 или повече гола. Ако
# футболистът е вкарал 10 или повече гола, програмата трябва да спре.
# Вход:
# От конзолата се четат по два реда до въвеждане на команда "END":
# •	Име на играч – текст
# •	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
# Изход:
# На конзолата да се отпечатат 2 реда :
# •	На първия ред:
#             "{име на играч} is the best player!"
# •	На втория ред :
# o	 Ако най-добрият футболист е направил хеттрик:
#                    "He has scored {брой голове} goals and made a hat-trick !!!"
# o	Ако най-добрият футболист не е направил хеттрик:
#                    "He has scored {брой голове} goals."

input_line = input()
hat_trick = False
the_best_player = ''
max_goals = 0

while input_line != 'END':
    name_player = input_line
    goals_number = int(input())

    if goals_number >= 10:
        the_best_player = name_player
        max_goals = goals_number
        hat_trick = True
        break
    else:
        if goals_number > max_goals:
            max_goals = goals_number
            the_best_player = name_player

            if goals_number >= 3:
                hat_trick = True

    input_line = input()

print(f'{the_best_player} is the best player!')

if hat_trick:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')