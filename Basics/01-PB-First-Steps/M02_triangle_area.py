# Напишете програма, която чете от конзолата страна и височина на триъгълник и пресмята неговото лице.
# Използвайте формулата за лице на триъгълник: area = a * h / 2. Форматирате изхода до втория знак след
# десетичната запетая.

a = float(input())
h = float(input())

area = (a*h)/2

print(f'{area:.2f}')