# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer

# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.

# Print the result of the subtract() function on the console.

def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(result, third_number):
    return result - third_number


def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    return subtract(result, third)


num1, num2, num3 = int(input()), int(input()), int(input())

print(add_and_subtract(num1, num2, num3))