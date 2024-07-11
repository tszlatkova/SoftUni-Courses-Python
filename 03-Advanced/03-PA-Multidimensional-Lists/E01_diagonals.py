# Using a nested list comprehension, write a program that reads rows of a square matrix
# and its elements, separated by a comma and a space ", ". You should find the matrix's
# diagonals, print them, and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

n = int(input())
matrix = []
primary_diagonal, secondary_diagonal = [], []

for _ in range(n):
    matrix.append([int(el) for el in input().split(', ')])

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-i-1])

sum_first = sum(primary_diagonal)
sum_second = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. "
      f"Sum: {sum_first}")

print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. "
      f"Sum: {sum_second}")
