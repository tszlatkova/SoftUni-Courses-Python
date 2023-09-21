# Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за боядисване са:
# •	червено (red)
# •	оранжев (orange)
# •	син (blue)
# •	зелен (green)
# Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят и от кой цвят яйцата са най - много,
# като знаете общия им брой и цвета на всяко яйце.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# o	Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"
# Изход
# Да се отпечатат на конзолата 5 реда:
# •	"Red eggs: {брой на червените яйца}"
# •	"Orange eggs: {брой на оранжевите яйца}"
# •	"Blue eggs: {брой на сините яйца}"
# •	"Green eggs: {брой на зелените яйца}"
# •	"Max eggs: {максимален брой на яйцата от цвят} -> {цвят}"

painted_eggs = int(input())

count_red, count_orange, count_blue, count_green = 0, 0, 0, 0

for _ in range(1, painted_eggs + 1):
    colour_egg = input()

    if colour_egg == 'red':
        count_red += 1
    elif colour_egg == 'orange':
        count_orange += 1
    elif colour_egg == 'blue':
        count_blue += 1
    elif colour_egg == 'green':
        count_green += 1

colours_count = [count_red, count_orange, count_blue, count_green]
colours_name = ['red', 'orange', 'blue', 'green']

max_colour = colours_name[colours_count.index(max(colours_count))]

print(f"Red eggs: {count_red}")
print(f"Orange eggs: {count_orange}")
print(f"Blue eggs: {count_blue}")
print(f"Green eggs: {count_green}")
print(f"Max eggs: {max(colours_count)} -> {max_colour}")