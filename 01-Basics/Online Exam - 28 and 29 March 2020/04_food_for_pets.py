# Ани има два домашни любимеца - куче и котка. Напишете програма, която изготвя статистика за храната
# на домашните любимци за определен брой дни. Всеки ден кучето и котката изяждат различно количество от
# общата им храна. На всеки трети ден получават награда - бисквитки. Количеството на бисквитките е 10%
# от общо изядената храна за деня.
# Вашата програма трябва да отпечатва статистика за количеството бисквитки, които са изяли, колко процента
# от първоначалното количество обща храна са изяли и колко процента от изядената храна е изяло кучето
# и колко е изяла котката.
# Вход
# Първоначално се чете един ред:
# •	Брой дни – цяло число в диапазона [1…30]
# •	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# o	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# o	Количество изядена храна от котката – цяло число в диапазона [10…500]
# Изход
# На конзолата да се отпечатват четири реда:
# •	"Total eaten biscuits: {количество изядени бисквитки}gr."
# •	"{процент изядена храна}% of the food has been eaten."
# •	"{процент изядена храна от кучето}% eaten from the dog."
# •	"{процент изядена храна от котката}% eaten from the cat."
# Количеството изядени бисквитки трябва да бъде закръглено до най – близкото цяло число, а процентът храна трябва да бъде форматиран до втората цифра след десетичния знак.

days = int(input())
total__left_food = float(input())

total_food_dog = 0
total_food_cat = 0
biscuits = 0
total_eaten_food = 0

for day in range (1, days + 1):
    food_dog_for_the_day = int(input())
    food_cat_for_the_day = int(input())

    total_food_dog += food_dog_for_the_day
    total_food_cat += food_cat_for_the_day
    total_eaten_food += food_cat_for_the_day + food_dog_for_the_day

    if day % 3 == 0:
        biscuits += (food_dog_for_the_day + food_cat_for_the_day) * 0.10

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total_eaten_food / total__left_food * 100:.2f}% of the food has been eaten.')
print(f'{total_food_dog / total_eaten_food * 100:.2f}% eaten from the dog.')
print(f'{total_food_cat / total_eaten_food * 100:.2f}% eaten from the cat.')