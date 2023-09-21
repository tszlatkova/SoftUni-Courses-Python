# Вашата задача е да напишете програма, която да изчислява, дали даден играч е успял да спечели лег. (Лег се нарича единична игра на дартс)
# Първоначално играчът започва с 301 точки. Играчът хвърля стрелата върху таблото, като за всяко улучено поле, той получава определен брой точки. Всяко поле има по три сектора: единичен (Single) сектор от който се взимат броят точки от полето. Двоен (Double), от него се взимат удвоените точки от полето и троен (Triple) сектор, точките от който са умножени по 3.
# Получените точки от всеки изстрел се изваждат от началните точки, до достигане на 0.
# Забележка: При изстрел, даващ повече точки от наличните, той се зачита за неуспешен и играчът трябва да хвърля отново,
# докато не уцели точки равни на оставащите или по-малки, такъв удар се счита за успешен.
# Пример: При налични точки 100, удар даващ повече от 100 точки, неуспешен
# При налични точки 100, удар даващ по-малко или равни на 100 точки, успешен
# Вход
# Първоначално се чете един ред:
# •	Името на играча - текст
# След това до получаване на команда "Retire" се четат многократно по два реда:
# 1.	Поле – текст ("Single", "Double" или "Triple")
# 2.	Точки – цяло число в интервала [0… 100]
# Изход
# Играта приключва при въвеждане на команда "Retire" или при изравняване на началните 301 точки към 0. На конзолата
# трябва да се напечата един ред:
# •	Ако играчът е спечелил лега:
# o	"{името на играча} won the leg with {успешните изстрели} shots."
# •	Ако играчът се е отказал от играта:
# o	"{името на играча} retired after {неуспешни изстрели} unsuccessful shots."

name = input()

starting_points = 301
input_line = input()
successful_shots = 0
unsuccessful_shots = 0
won = False

while input_line != 'Retire':
    area = input_line
    points = int(input())

    if area == 'Single':
        not_sure_points = starting_points - points

        if not_sure_points < 0:
            unsuccessful_shots += 1
            input_line = input()
            continue
        elif not_sure_points == 0:
            won = True
            successful_shots += 1
            break
    elif area == 'Double':
        not_sure_points = starting_points - points * 2

        if not_sure_points < 0:
            unsuccessful_shots += 1
            input_line = input()
            continue
        elif not_sure_points == 0:
            won = True
            successful_shots += 1
            break
    elif area == 'Triple':
        not_sure_points = starting_points - points * 3

        if not_sure_points < 0:
            unsuccessful_shots += 1
            input_line = input()
            continue
        elif not_sure_points == 0:
            won = True
            successful_shots += 1
            break

    starting_points = not_sure_points
    successful_shots += 1
    input_line = input()

if won:
    print(f'{name} won the leg with {successful_shots} shots.')
else:
    print(f'{name} retired after {unsuccessful_shots} unsuccessful shots.')