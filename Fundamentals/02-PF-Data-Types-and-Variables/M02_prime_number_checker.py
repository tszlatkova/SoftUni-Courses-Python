# Write a program to check if a number is prime. A prime number is a natural number greater than 1, not a
# product of two smaller natural numbers. For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1,
# involve 5 itself.
#
# The input comes as an integer number.
#
# The output should be True if the number is prime and False otherwise.

number = int(input())

is_prime = False

for i in range(1, number):
    if i == 1:
        is_prime = False

        if number == 2:
            is_prime = True

    else:
        if number % i == 0:
            is_prime = False
            break
        else:
            is_prime = True

print(is_prime)