# По време на седмицата на Оскарите, градското кино пуска прожекции на някои от филмите, които са номинирани в
# категорията за "Най-добър филм". В таблицата са показани кои са филмите и каква е цената за прожекция спрямо залата,
# в която се прожектира филмът.
# Филм                      	normal          	luxury          	ultra luxury
# A Star Is Born	            7.50 лв.	        10.50 лв.	        13.50 лв.
# Bohemian Rhapsody	            7.35 лв.	        9.45 лв.	        12.75 лв.
# Green Book	                8.15 лв.	        10.25 лв.	        13.25 лв.
# The Favourite	                8.75 лв.	        11.55 лв.       	13.95 лв.

# Напишете програма, която изчислява какъв е приходът от даден филм, като знаете в какъв тип зала се прожектира и
# колко човека са си купили билет за прожекцията.

# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – име на филм – текст ("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
# •	Втори ред– вид на залата – текст ("normal", "luxury" или "ultra luxury")
# •	Трети ред – брой на закупените билети – цяло число в интервала [1…100]

# Изход
# На конзолата трябва да се отпечата един ред:
# "{име на филма} -> {приходи от прожекцията на филма} lv."
# Приходите да бъдат закръглени до втория знак след десетичната запетая.

film_name = input()
room_type = input()
tickets_number = int(input())

if film_name == 'A Star Is Born':
    if room_type == 'normal':
        price_per_ticket = 7.50
    elif room_type == 'luxury':
        price_per_ticket = 10.50
    elif room_type == 'ultra luxury':
        price_per_ticket = 13.50
elif film_name == 'Bohemian Rhapsody':
    if room_type == 'normal':
        price_per_ticket = 7.35
    elif room_type == 'luxury':
        price_per_ticket = 9.45
    elif room_type == 'ultra luxury':
        price_per_ticket = 12.75
elif film_name == 'Green Book':
    if room_type == 'normal':
        price_per_ticket = 8.15
    elif room_type == 'luxury':
        price_per_ticket = 10.25
    elif room_type == 'ultra luxury':
        price_per_ticket = 13.25
elif film_name == 'The Favourite':
    if room_type == 'normal':
        price_per_ticket = 8.75
    elif room_type == 'luxury':
        price_per_ticket = 11.55
    elif room_type == 'ultra luxury':
        price_per_ticket = 13.95

total_income = tickets_number * price_per_ticket

print(f"{film_name} -> {total_income:.2f} lv.")