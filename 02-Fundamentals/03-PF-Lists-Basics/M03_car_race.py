# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step
# (the index). There will be two cars. The first one starts from the left side, and the other one starts from the
# right side. The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time
# (the racer with less time). If you have a zero in the list, you should reduce the racer's time that reached it
# by 20% (from his current time).
# The number of elements in the sequence will always be odd.

# Print the result in the following format
# "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

input_line = [int(i) for i in input().split(' ')]

middle_index = len(input_line)//2

first_racer = input_line[:middle_index]
second_racer = input_line[len(input_line)-1:middle_index:-1]
first_racer_time = 0
second_racer_time = 0

for i in range(len(first_racer)):
    if first_racer[i] == 0:
        first_racer_time = first_racer_time * 0.80
    else:
        first_racer_time += first_racer[i]

    if second_racer[i] == 0:
        second_racer_time = second_racer_time * 0.80
    else:
        second_racer_time += second_racer[i]

if first_racer_time < second_racer_time:
    print(f'The winner is left with total time: {first_racer_time:.1f}')
elif first_racer_time > second_racer_time:
    print(f'The winner is right with total time: {second_racer_time:.1f}')