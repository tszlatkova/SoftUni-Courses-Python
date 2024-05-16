# Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг /
# окръжност с радиус r, като форматирате изхода в следния вид: "<calculated area>"
# "<calculated parameter>". Форматирайте изходните данни до втория знак след десетичната запетая.

from math import pi

r = float(input())

area = r**2*pi
perimeter = 2*pi*r

print(f'{area:.2f}')
print(f'{perimeter:.2f}')