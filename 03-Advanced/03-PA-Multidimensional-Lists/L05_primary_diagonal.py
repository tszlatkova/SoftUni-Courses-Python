# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs
# from top left to bottom right). On the first line, you will receive an integer N – the
# size of a square matrix. The next N lines hold the values for each column - N numbers,
# separated by a single space.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_primary_diagonal = 0

for index in range(n):
    sum_primary_diagonal += matrix[index][index]

print(sum_primary_diagonal)
