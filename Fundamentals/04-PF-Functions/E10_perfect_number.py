# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_number(number: int):

    perfect = False

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    if sum(divisors) == number:
        perfect = True

    return perfect


input_number = int(input())

if perfect_number(input_number):
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")