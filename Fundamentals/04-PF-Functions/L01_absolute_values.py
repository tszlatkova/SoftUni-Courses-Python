# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
# as a list. Use abs().

numbers = input().split(' ')
abs_numbers = []

for i in numbers:
    abs_numbers.append(abs(float(i)))

print(abs_numbers)