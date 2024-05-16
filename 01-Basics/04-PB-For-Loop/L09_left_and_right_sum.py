# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на
# първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

n = int(input())

sum1 = 0
sum2 = 0

for _ in range(n):
    number = int(input())
    sum1 += number

for _ in range(n):
    number = int(input())
    sum2 += number

if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    diff = abs(sum2 - sum1)
    print(f'No, diff = {diff}')