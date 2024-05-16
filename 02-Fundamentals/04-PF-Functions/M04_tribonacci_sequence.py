# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space,
# starting from 1. You will receive a positive integer number as input.

def tribonacci(number):
    tribonacci_list = [1]

    if number > 1:

        for i in range(1, number):
            if i == 1:
                tribonacci_list.append(1)
            elif i == 2:
                tribonacci_list.append(2)
            else:
                previous_three = tribonacci_list[i-1] + tribonacci_list[i-2] + tribonacci_list[i-3]
                tribonacci_list.append(previous_three)

    return tribonacci_list


input_number = int(input())

print(*tribonacci(input_number))