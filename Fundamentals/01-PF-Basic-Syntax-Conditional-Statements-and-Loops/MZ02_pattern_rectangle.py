# Draw a Rectangle: The user should specify the number of rows and columns for the rectangle. Example:
# Enter the number of rows for the rectangle: 4
# Enter the number of columns for the rectangle: 6
#
# ******
# ******
# ******
# ******

rows = int(input('Enter the number of rows for the rectangle: '))
columns = int(input('Enter the number of columns for the rectangle: '))

for _ in range(1, rows + 1):
    print(columns * '*', end = '\n')