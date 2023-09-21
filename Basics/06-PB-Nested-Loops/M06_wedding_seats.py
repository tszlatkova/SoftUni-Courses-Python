# Младоженците искат да направят списък кой на кое място ще седи на сватбената церемония. Местата са разделени на
# различни сектори. Секторите са главните латински букви като започват от A. Във всеки сектор има определен брой
# редове. От конзолата се чете броят на редовете в първия сектор (A), като във всеки следващ сектор редовете се
# увеличават с 1. На всеки ред има определен брой места - тяхната номерация е представена с малките латински букви.
# Броя на местата на нечетните редове се прочита от конзолата, а на четните редове местата са с 2 повече.
# Вход
# От конзолата се четaт 3 реда:
# •	Последния сектор от секторите - символ (B-Z)
# •	Броят на редовете в първия сектор - цяло число (1-100)
# •	Броят на местата на нечетен ред - цяло число (1-24)
# Изход
# Да се отпечата на конзолата всяко място на отделен ред по следния формат:
# {сектор}{ред}{място}
# Накрая трябва да отпечата броя на всички места.

last_sector = input()
first_sector_rows = int(input())
odd_rows_seats = int(input())

even_rows_seat = odd_rows_seats + 2
current_rows = first_sector_rows
total_seats = 0

for sector in range(ord('A'), (ord(last_sector) + 1)):

    for row in range(1, current_rows + 1):

        if row % 2 != 0:
            for seat in range(97, 97 + odd_rows_seats):
                print(f'{chr(sector)}{row}{chr(seat)}')
                total_seats += 1
        else:
            for seat in range(97, 97 + even_rows_seat):
                print(f'{chr(sector)}{row}{chr(seat)}')
                total_seats += 1

    current_rows += 1

print(total_seats)