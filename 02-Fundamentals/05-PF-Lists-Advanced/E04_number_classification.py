# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints
# all the positive, negative, even, and odd numbers on separate lines as shown below.

# Note: Zero is counted for a positive number

numbers = input().split(', ')

positive = [number for number in numbers if int(number) >= 0]
negative = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")