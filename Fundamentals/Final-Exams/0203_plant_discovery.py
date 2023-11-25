# You have now returned from your world tour. On your way, you have discovered some new plants, and you want
# to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about
# the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you
# will need it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.
# Input / Constraints
# •	You will receive the input as described above.
# •	JavaScript: you will receive a list of strings.
# Output
# •	Print the information about all plants as described above.

from statistics import mean

n_lines = int(input())
plants = {}

for _ in range(n_lines):
    plant, rarity = input().split('<->')

    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'ratings': []}
    else:
        plants[plant]['rarity'] = rarity

while True:
    command = input()

    if command == 'Exhibition':
        break

    command = command.split(': ')
    action = command[0]

    if 'Rate' == action or 'Update' == action:
        plant, rating_rarity = command[1].split(' - ')
    else:
        plant = command[1]

    if plant not in plants:
        print('error')
    else:
        if action == 'Rate':
            plants[plant]['ratings'].append(int(rating_rarity))
        elif action == 'Update':
            plants[plant]['rarity'] = rating_rarity
        elif action == 'Reset':
            plants[plant]['ratings'] = []

print(f'Plants for the exhibition:')

for plant in plants:
    rarity = int(plants[plant]['rarity'])
    ratings = plants[plant]['ratings']
    avg_rating = 0 if len(ratings) == 0 else mean(ratings)
    print(f'- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}')
