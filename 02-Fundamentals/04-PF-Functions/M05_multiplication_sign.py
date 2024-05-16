# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative,
# positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.

def count_negative_signs(list_numbers):
    count = 0

    if '0' in list_numbers:
        return 'zero'
    else:

        for i in range(3):
            if '-' in list_numbers[i]:
                count += 1

        if count % 2 == 0:
            return 'positive'
        else:
            return 'negative'


numbers = []

for _ in range(3):
    numbers.append(input())

print(count_negative_signs(numbers))