# Иван е измислил нова игра в която да се състезава със своите приятели. Вашата задача е да напишете програма за играта.
# Всеки играч написва името си, след това за всяка една буква от името си написва по едно цяло число, ако числото
# съвпада с ASCII стойността на съответната буква, играчът получава 10 точки, в противен случай, получава само 2 точки.
# Победител е играчът с най-много точки в края на играта. В случай, че двама играчи имат равен брой точки, печели този,
# който втори е достигнал резултата.
# Вход
# До получаване на командата "Stop" се чете по един ред:
# •	Име на играча с дължина n - текст
# За всеки играч се четат n на брой реда:
# •	число – цяло число в интервала[0…127]
# Изход
# Да се отпечата един ред в следния формат:
# •	"The winner is {името на победителя} with {точките на победителя} points!"

input_line = input()

max_total_points = 0
winner = ''

while input_line != 'Stop':
    name_player = input_line
    points_current_player = 0

    for letter in range(len(name_player)):
        number = int(input())

        if name_player[letter] == chr(number):
            points_current_player += 10
        else:
            points_current_player += 2

    if points_current_player >= max_total_points:
        max_total_points = points_current_player
        winner = name_player

    input_line = input()

print(f'The winner is {winner} with {max_total_points} points!')