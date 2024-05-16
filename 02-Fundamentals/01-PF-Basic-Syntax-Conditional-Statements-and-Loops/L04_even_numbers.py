# Write a program that receives a number n on the first line. On the following n lines, it receives different integer
# numbers. If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise,
# if all numbers given are even, print "All numbers are even.".

numbers = int(input())
odd_number = False
current_number = int()

for i in range(1, numbers + 1):
    current_number = int(input())
    if current_number % 2 != 0:
        odd_number = True
        break

if odd_number:
    print(f'{current_number} is odd!')
else:
    print('All numbers are even.')