# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.

number = int(input())

solutions_count = 0

for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number +1):
            if x1 + x2 + x3 == number:
                solutions_count += 1

print(solutions_count)