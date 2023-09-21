# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата, минимума и максимума на
# числата на четни и нечетни позиции (броим от 1). Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.

import sys

n = int(input())

OddSum = 0
OddMin = sys.maxsize
OddMax = - sys.maxsize
EvenSum = 0
EvenMin = sys.maxsize
EvenMax = - sys.maxsize

for position in range(1, n + 1):
    number = float(input())

    if position % 2 != 0:
        OddSum += number

        if number > OddMax:
            OddMax = number

        if number < OddMin:
            OddMin = number

    else:
        EvenSum += number

        if number > EvenMax:
            EvenMax = number

        if number < EvenMin:
            EvenMin = number

print(f'OddSum={OddSum:.2f},')

if OddMin == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={OddMin:.2f},')

if OddMax == - sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={OddMax:.2f},')

print(f'EvenSum={EvenSum:.2f},')

if EvenMin == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={EvenMin:.2f},')

if EvenMax == - sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={EvenMax:.2f}')