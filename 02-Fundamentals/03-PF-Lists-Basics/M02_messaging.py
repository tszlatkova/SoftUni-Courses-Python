# On the first line, you will receive a sequence of numbers separated by a single space. On the second line,
# you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. Each char the
# program adds to the message should be found by its index. The index you are looking for is the sum of a number's
# digits from the first sequence. If the index is greater than the length of the text, continue counting from the
# beginning (so that you always have a valid index). When you find a char, you should add it to the message and
# remove it from the string. It means that for the following index, the text will contain one character less.
# Print the final message.

input_line = input().split(' ')
code = [s for s in input()]

message = ''

for i in range(len(input_line)):
    sum_digits = 0

    for number in input_line[i]:
        sum_digits += int(number)

    if sum_digits >= len(code):
        index = sum_digits % len(code)
    else:
        index = sum_digits

    letter = code.pop(index)
    message += letter

print(message)
