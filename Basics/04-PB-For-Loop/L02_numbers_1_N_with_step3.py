# Напишете програма, която чете число n, въведено от потребителя и отпечатва числата от 1 до n през 3.

n = int(input())

for i in range(1, n +1, 3):
    print(i)