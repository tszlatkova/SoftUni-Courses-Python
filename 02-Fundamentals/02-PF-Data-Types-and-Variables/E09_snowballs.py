# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best
# snowballs. They have decided to involve you in their fray by writing a program that calculates snowball data and
# outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.

# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball.

# Output
# •	You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

snowballs = int(input())  # integer in range [0, 100]

highest_value = 0

for _ in range(0, snowballs):
    weight = int(input())  # integer in the range [0, 1000]
    time = int(input())  # integer in the range [1, 500]
    quality = int(input())  # integer in the range [0, 100]

    snowball_value = (weight / time) ** quality

    if snowball_value > highest_value:
        highest_value = snowball_value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f'{snowball_weight} : {snowball_time} = {int(highest_value)} ({snowball_quality})')