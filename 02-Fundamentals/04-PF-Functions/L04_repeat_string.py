# Write a function that receives a string and a counter n. The function should return a new string – the result of
# repeating the old string n times. Print the result of the function. Try using lambda.

input_line = input()
repeat_number = int(input())

repeat_string = lambda word, count: word * count

print(repeat_string(input_line, repeat_number))