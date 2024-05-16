# You will receive a single number. You should write a function that returns the sum of all even and all odd digits
# in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def odd_even_sum(str_number):
    odd_sum, even_sum = [], []

    for i in range(len(str_number)):
        number = int(str_number[i])

        if number % 2 == 0:
            even_sum.append(number)
        else:
            odd_sum.append(number)

    return sum(odd_sum), sum(even_sum)


input_line = input()
result = odd_even_sum(input_line)

print(f'Odd sum = {result[0]}, Even sum = {result[1]}')