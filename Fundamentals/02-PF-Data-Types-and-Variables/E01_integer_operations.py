# Write a program that reads four integer numbers. It should add the first to the second number, integer divide the
# sum by the third number, and multiply the result by the fourth number. Print the final result.

# In Python, we can perform floor division (also sometimes known as integer division) using the // operator.

numbers = []

for i in range(0,4):
    numbers.append(int(input()))

result = ((numbers[0] + numbers[1]) // numbers[2]) * numbers[3]

print(result)