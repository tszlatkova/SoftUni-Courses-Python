# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(number):
    result = 1

    for i in range(number, 1, -1):
        result *= i

    return result


num1, num2 = int(input()), int(input())

division = factorial(num1) / factorial(num2)

print(f'{division:.2f}')