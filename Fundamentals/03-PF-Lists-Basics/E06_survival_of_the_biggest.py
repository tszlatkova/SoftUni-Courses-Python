# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones, and then,
# you should print all the numbers that are left in the list, separated by a comma and a space ", ".

integers_list = list(map(int,input().split(' ')))
number = int(input())

integers_list_sorted = sorted(integers_list)

for number in range(number):
    integers_list.remove(integers_list_sorted[number])

print(*integers_list, sep = ', ')