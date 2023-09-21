# Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.  Всеки ден
# получавате имена на игри до команда "Finish". Със спечелването на всяка една игра печелите по 20лв. за
# благотворителност. Трябва да изчислите колко пари сте спечелили на края на деня. Ако имате повече спечелени игри,
# отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%. При приключване на турнира ако
# през повечето дни сте били победители печелите турнира и увеличавате всичките спечелени пари с 20%.
# Никога няма да имате равен брой спечелени и загубени игри.
# Вход
# Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
# До получаване на командата "Finish" се чете:
# •	Спорт  – текст
# За всеки спорт се прочита:
# o	Резултат  – текст с възможности: "win" или "lose"
# Изход
# Накрая се отпечатва един ред:
# •	Ако сте спечелили турнира:
#      	"You won the tournament! Total raised money: {спечелените пари}"
# •	Ако сте загубили на турнира:
# "You lost the tournament! Total raised money: {спечелените пари}"
# Парите да бъдат форматирани до втората цифра след десетичния знак.

days = int(input())
total_wins = 0
total_lost = 0
total_income = 0

for _ in range(1, days + 1):
    input_line = input()
    win_games = 0
    lost_games = 0
    income_for_the_day = 0

    while input_line != 'Finish':
        sport = input_line
        outcome = input()

        if outcome == 'win':
            win_games += 1
            income_for_the_day += 20
        elif outcome == 'lose':
            lost_games += 1

        input_line = input()

    if win_games > lost_games:
        income_for_the_day = 1.10 * income_for_the_day

    total_income += income_for_the_day
    total_wins += win_games
    total_lost += lost_games

if total_wins > total_lost:
    total_income *= 1.20
    print(f'You won the tournament! Total raised money: {total_income:.2f}')
elif total_lost > total_wins:
    print(f'You lost the tournament! Total raised money: {total_income:.2f}')