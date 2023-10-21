# erry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and
# buys him everything he needs – food, hay, and cover.
# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30
# days). On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of hay
# equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
# •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0].
# •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0].
# •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0].
# •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0].
# Output
# •	If the food, the hay, and the cover are enough, print:
# o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
# •	If one of the things is not enough, print:
# o	"Merry must go to the pet store!"
# The output values must be formatted to the second decimal place!

food_kg, hay_kg, cover_kg, weight_kg = float(input()), float(input()), float(input()), float(input())

count_days = 0
not_enough = False

while count_days < 30:
    count_days += 1

    food_kg -= 0.3

    if count_days % 2 == 0:
        hay_kg -= 0.05 * food_kg

    if count_days % 3 == 0:
        cover_kg -= 1/3 * weight_kg

    if round(food_kg,2) <= 0 or round(hay_kg,2) <= 0 or round(cover_kg,2) <= 0:
        not_enough = True
        break

if not_enough:
    print(f'Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.')