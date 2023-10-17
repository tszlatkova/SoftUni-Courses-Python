# Using comprehension, write a program that receives some text, separated by space, and take only those words whose
# length is even. Print each word on a new line.

input_line = input().split(' ')

even_length = [word for word in input_line if len(word) % 2 == 0]

for i in range(len(even_length)):
    print(even_length[i])