# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви
# даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава
# се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор
# е получил номинация.
# Вход
# •	Име на актьора – текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n – цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o	Име на оценяващия – текст
# o	Точки от оценяващия – реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# •	Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!

actor_name = input()
actor_academy_points = float(input())
evaluators_number = int(input())

actor_total_points = actor_academy_points
enough_points = False

for _ in range(1, evaluators_number + 1):
    evaluator_name = input()
    evaluator_points = float(input())

    actor_total_points += len(evaluator_name) * evaluator_points / 2

    if actor_total_points > 1250.50:
        enough_points = True
        break

if enough_points:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {actor_total_points:.1f}!')
else:
    diff = 1250.50 - actor_total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')