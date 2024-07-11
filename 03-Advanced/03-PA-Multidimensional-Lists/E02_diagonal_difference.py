# Write a program that finds the difference between the sums of the square matrix
# diagonals (absolute value).

# On the first line, you will receive an integer N - the size of a square matrix. The
# following N lines hold the values for each column - N numbers separated by a single
# space. Print the absolute difference between the primary and the secondary diagonal
# sums.

n = int(input())
matrix = []
primary_diagonal, secondary_diagonal = [], []

for _ in range(n):
    matrix.append([int(el) for el in input().split(' ')])

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-i-1])

sum_first = sum(primary_diagonal)
sum_second = sum(secondary_diagonal)

print(abs(sum_first - sum_second))
