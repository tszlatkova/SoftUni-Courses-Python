# Create a program that receives two strings on a single line separated by a single space. Then, it prints the
# sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum,
# then continue with the next two characters. If one of the strings is longer than the other, add the remaining
# character codes to the total sum without multiplication.

first_string, second_string = input().split(' ')

sum_total = 0

if len(first_string) > len(second_string):
    for char in range(len(second_string)):
        sum_total += ord(first_string[char]) * ord(second_string[char])
    for char in range(len(second_string), len(first_string)):
        sum_total += ord(first_string[char])

elif len(first_string) < len(second_string):
    for char in range(len(first_string)):
        sum_total += ord(first_string[char]) * ord(second_string[char])
    for char in range(len(first_string), len(second_string)):
        sum_total += ord(second_string[char])
else:
    for char in range(len(first_string)):
        sum_total += ord(first_string[char]) * ord(second_string[char])

print(sum_total)
