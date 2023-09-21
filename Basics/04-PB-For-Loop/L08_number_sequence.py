# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

n = int(input())

# create an empty list
numbers = []

for _ in range(1, n+1):
    number = int(input())
    numbers.append(number)

max_number = max(numbers)
min_number = min(numbers)

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')