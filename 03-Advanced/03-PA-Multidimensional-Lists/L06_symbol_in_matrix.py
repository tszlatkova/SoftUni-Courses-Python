# Write a program that reads a number - N, representing the rows and columns of a square
# matrix. On the next N lines, you will receive rows of the matrix. Each row consists of
# ASCII characters. After that, you will receive a symbol. Find the first occurrence of
# that symbol in the matrix and print its position in the format: "({row}, {col})". It
# would help if you started searching from the top left. If there is no such symbol, print
# the message "{symbol} does not occur in the matrix".

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([char for char in input()])

symbol_to_search = input()
symbol_found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol_to_search:
            print(f'({row}, {col})')
            symbol_found = True
            exit()

if not symbol_found:
    print(f'{symbol_to_search} does not occur in the matrix')
