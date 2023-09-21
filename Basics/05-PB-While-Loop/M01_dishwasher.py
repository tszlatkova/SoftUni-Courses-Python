# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от
# препарат за съдомиялна е достатъчно, за да измие определено количество съдове. Знае се,
# че всяка бутилка съдържа 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.
# Приемете, че на всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери,
# а останалите пъти с чинии. Докато не получите команда "End" ще продължите да получавате бройка съдове,
# които трябва да бъдат измити.
# Вход
# От конзолата се четат:
# •	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи,
# брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
# Изход
# В случай, че количеството препарат е било достатъчно за измиването на съдовете:
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"

bottles = int(input())

total_detergent = bottles * 750
count = 0
for_washing = input()
warning = False
clean_dishes = 0
clean_pots = 0

while for_washing != 'End':
    dishes_or_pot = int(for_washing)
    count += 1

    if count % 3 == 0:
        total_detergent -= dishes_or_pot * 15
    else:
        total_detergent -= dishes_or_pot * 5

    if total_detergent < 0:
        warning = True
        break

    if count % 3 == 0:
        clean_pots += dishes_or_pot
    else:
        clean_dishes += dishes_or_pot

    for_washing = input()

if warning:
    print(f'Not enough detergent, {abs(total_detergent)} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{clean_dishes} dishes and {clean_pots} pots were washed.')
    print(f'Leftover detergent {total_detergent} ml.')