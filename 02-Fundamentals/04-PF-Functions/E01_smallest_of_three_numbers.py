# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.

list_numbers = []

for _ in range(3):
    list_numbers.append(int(input()))

print(min(list_numbers))