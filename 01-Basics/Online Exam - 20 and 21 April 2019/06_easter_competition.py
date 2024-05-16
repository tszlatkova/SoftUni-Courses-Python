# С наближаването на Великден, пекарна организира конкурс за направата на най-хубав козунак.
# Напишете програма, която да намира сладкаря с най-висок резултат. В началото на конкурса се въвежда броя на
# козунаците, които ще бъдат дегустирани от посетителите на пекарната, като за всеки козунак различен брой
# посетители, ще дадат оценка от 1 до 10.
# Вход
# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# •	Името на пекаря, който е направил козунака – текст
# •	До получаване на командата "Stop" се прочита
# o	оценка за козунак от един човек  – цяло число в интервала [1... 10]
# Изход
# След получаване на командата "Stop" се печата един ред:
# •	"{името на пекаря} has {общият брой получени точки} points."
# Ако след командата "Stop", пекарят е с най-много точки до момента, да се отпечата допълнителен ред:
# •	"{името на пекаря} is the new number 1!"
# След дегустация на всички козунаци, да се отпечата един ред:
# •	"{името на пекаря с най-много точки} won competition with {точките на пекаря} points!"

number_easter_cakes = int(input())
max_points = 0
the_best_baker = ''

for _ in range(1, number_easter_cakes + 1):
    baker_name = input()
    input_line = input()
    total_points = 0

    while input_line != 'Stop':
        rating = int(input_line)

        total_points += rating

        input_line = input()

    print(f'{baker_name} has {total_points} points.')

    if total_points > max_points:
        print(f'{baker_name} is the new number 1!')
        max_points = total_points
        the_best_baker = baker_name

print(f'{the_best_baker} won competition with {max_points} points!')