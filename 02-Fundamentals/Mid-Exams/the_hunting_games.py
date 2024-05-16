days = int(input())
players = int(input())
group_energy = float(input())
water_per_day_person = float(input())
food_per_day_person = float(input())

count_days = 0
not_enough_energy = False
total_water = players * water_per_day_person * days
total_food = players * food_per_day_person * days

while count_days != days:

    count_days += 1

    chop_wood_energy = float(input())

    if group_energy - chop_wood_energy <= 0:
        not_enough_energy = True
        break
    else:
        group_energy -= chop_wood_energy

    if count_days % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.70

    if count_days % 3 == 0:
        total_food -= total_food/players
        group_energy *= 1.10

if not_enough_energy:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
else:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')