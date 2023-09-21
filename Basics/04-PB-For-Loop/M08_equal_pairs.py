# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н. Всяка двойка
# има стойност – сумата от съставящите я числа. Напишете програма, която проверява дали всички двойки имат еднаква
# стойност или печата максималната разлика между две последователни двойки. Ако всички двойки имат еднаква стойност,
# отпечатайте "Yes, value={Value}" + стойността. В противен случай отпечатайте "No, maxdiff={Difference}"
# + максималната разлика.

import sys

pairs = int(input())
first_number = int(input())
second_number = int(input())
previous_sum = first_number + second_number

diff = 0
equal = True
sum_pair = 0
max_diff = -sys.maxsize

if pairs > 1:
    for i in range(2, pairs + 1):
        number1 = int(input())
        number2 = int(input())
        sum_pair = number1 + number2

        if sum_pair == previous_sum:
            equal = True
        else:
            diff = abs(sum_pair - previous_sum)
            equal = False
            if diff > max_diff:
                max_diff = diff

        previous_sum = sum_pair

elif pairs == 1:
    equal = True

if equal:
    print(f'Yes, value={previous_sum}')
else:
    print(f'No, maxdiff={max_diff}')