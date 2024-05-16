# Write a program that reads different floating-point numbers from the console. When it receives a number between
# 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".

input_number = float(input())

while input_number < 1 or input_number > 100:
    input_number = float(input())

print(f'The number {input_number} is between 1 and 100')