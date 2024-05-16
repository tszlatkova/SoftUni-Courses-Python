# Футболен отбор участва в благотворителен турнир. На този турнир отборът играе три мача като домакин. Да се напише
# програма, която изчислява колко победи, равенства и загуби има отборът по време на турнира, спрямо резултатите от
# мачовете.
# *Забележка: Отборът винаги е домакин, следователно първата цифра от резултата съответства на головете вкарани от него.
# Вход
# От конзолата се четат 3 реда:
# 1.	Резултат от първия мач – текст
# 2.	Резултат от втория мач – текст
# 3.	Резултат от третия мач – текст
# Резултатите ще са в следния формат: "2:0", "0:1", "1:1" и т.н.
# /броят голове винаги ще бъде едноцифрено число/
# Изход
# На конзолата да се отпечатат три реда:
# •	"Team won {брой спечелени мачове} games."
# •	"Team lost {брой загубени мачове} games."
# •	" Drawn games: {брой равни мачове}"

first_score = input()
second_score = input()
third_score = input()

win_count = 0
drawn_count = 0
lost_count = 0

if first_score[0] > first_score[2]:
    win_count += 1
elif first_score[0] == first_score[2]:
    drawn_count += 1
else:
    lost_count += 1

if second_score[0] > second_score[2]:
    win_count += 1
elif second_score[0] == second_score[2]:
    drawn_count += 1
else:
    lost_count += 1

if third_score[0] > third_score[2]:
    win_count += 1
elif third_score[0] == third_score[2]:
    drawn_count += 1
else:
    lost_count += 1

print(f'Team won {win_count} games.')
print(f'Team lost {lost_count} games.')
print(f'Drawn games: {drawn_count}')