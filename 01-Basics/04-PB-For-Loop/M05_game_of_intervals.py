moves = int(input())

result = 0
count1, count2, count3, count4, count5, invalid = 0, 0, 0, 0, 0, 0

for _ in range(1, moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        result += 0.20 * number
        count1 += 1
    elif 10 <= number <= 19:
        result += 0.30 * number
        count2 += 1
    elif 20 <= number <= 29:
        result += 0.40 * number
        count3 += 1
    elif 30 <= number <= 39:
        result += 50
        count4 += 1
    elif 40 <= number <= 50:
        result += 100
        count5 += 1
    else:
        result = result / 2
        invalid += 1

print(f'{result:.2f}')
print(f'From 0 to 9: {count1/moves*100:.2f}%')
print(f'From 10 to 19: {count2/moves*100:.2f}%')
print(f'From 20 to 29: {count3/moves*100:.2f}%')
print(f'From 30 to 39: {count4/moves*100:.2f}%')
print(f'From 40 to 50: {count5/moves*100:.2f}%')
print(f'Invalid numbers: {invalid/moves*100:.2f}%')