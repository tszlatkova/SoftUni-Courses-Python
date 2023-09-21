# Предстои Великден и Деси е решила да изпече домашни козунаци за колегите си. Главните продукти, които ще трябват на
# Деси са: брашно и захар. Един пакет захар е 950 грама, а един пакет брашно е 750 грама. Напишете програма, която
# изчислява колко пакета захар и брашно трябва да купи Деси, за да й стигнат за направата на козунаците, като знаете
# за всеки един козунак по колко грама захар и брашно са изразходени. Също намерете кое е най-голямото количество захар
# и брашно, които са използвани.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# o	Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# o	Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]
# Изход
# Да се отпечатат на конзолата 3 реда:
# •	"Sugar: {брой нужни пакети захар}"
# •	"Flour: {брой нужни пакет брашно}"
# •	"Max used flour is {максимално количество грамове брашно, използвани за правенето на козунак} grams, max used sugar
# is {максимално количество грамове захар, използвани за правенето на козунак} grams."
# Пакетите захар и брашно да бъдат закръглени към най-близкото цяло число нагоре.

from math import ceil

easter_cake = int(input())
max_sugar = 0
max_flour = 0
total_sugar = 0
total_flour = 0

for _ in range(1, easter_cake + 1):
    sugar_gr = int(input())
    flour_gr = int(input())

    total_sugar += sugar_gr
    total_flour += flour_gr

    if sugar_gr > max_sugar:
        max_sugar = sugar_gr

    if flour_gr > max_flour:
        max_flour = flour_gr

sugar_packets = ceil(total_sugar / 950)
flour_packets = ceil(total_flour / 750)

print(f'Sugar: {sugar_packets}')
print(f'Flour: {flour_packets}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')