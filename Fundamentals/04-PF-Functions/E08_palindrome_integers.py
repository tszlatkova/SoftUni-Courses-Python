# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that
# receives a list of positive integers, separated by comma and space ", ". The function should check if each integer is
# a palindrome - True or False. Print the result.

def palindrome(number):
    backward_number = ''

    for i in range(len(number) - 1, -1, -1):
        backward_number += number[i]

    return number == backward_number


numbers = input().split(', ')

for i in range(len(numbers)):
    print(palindrome(numbers[i]))

