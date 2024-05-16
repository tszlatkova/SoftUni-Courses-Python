# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които зависят от
# позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири, като знаете
# с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири и колко процента
# от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира до втората цифра
# след десетичния знак.

from math import floor

tournaments_number = int(input())
starting_points = int(input())

total_points = starting_points
tournaments_count = 0
tournaments_winner = 0

for _ in range(tournaments_number):
    stage_of_tournament = input()
    tournaments_count += 1
    if stage_of_tournament == 'W':
        total_points += 2000
        tournaments_winner += 1
    elif stage_of_tournament == 'F':
        total_points += 1200
    elif stage_of_tournament == 'SF':
        total_points += 720

average_points = floor((total_points - starting_points) / tournaments_count)
winner_percentage = tournaments_winner / tournaments_count * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{winner_percentage:.2f}%')