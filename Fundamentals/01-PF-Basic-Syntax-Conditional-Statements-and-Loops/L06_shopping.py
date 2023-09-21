# Write a program that reads an integer number representing a budget. On the following lines, it reads integer
# numbers representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!"
# and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

budget = int(input())
input_line = input()
not_enough_money = False

while input_line != 'End':
    input_line = int(input_line)

    if input_line <= budget:
        budget -= input_line
    else:
        not_enough_money = True
        break

    input_line = input()

if not_enough_money:
    print(f'You went in overdraft!')
else:
    print(f'You bought everything needed.')