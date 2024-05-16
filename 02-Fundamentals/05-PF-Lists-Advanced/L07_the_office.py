# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employees_happiness = list(map(int, input().split(' ')))
factor = int(input())

total_count = len(employees_happiness)
happy_count = 0

new_happiness = [factor * employees_happiness[i] for i in range(len(employees_happiness))]
average_happiness = sum(new_happiness) / total_count

for i in range(total_count):
    if new_happiness[i] >= average_happiness:
        happy_count += 1

if happy_count >= total_count // 2:
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')