# Напишете програма, която прочита едно число n, след това прочита n на брой цели числа и принтира средно
# аритметичното на тяхната сума число, форматирано до втората цифра след десетични знак.

n = int(input())
sum_numbers = 0

for _ in range(1, n + 1):
    number = int(input())
    sum_numbers += number

print(f'{sum_numbers / n:.2f}')