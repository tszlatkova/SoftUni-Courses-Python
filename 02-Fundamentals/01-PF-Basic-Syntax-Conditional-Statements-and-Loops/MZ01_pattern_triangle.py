# Draw a Triangle: The user should specify the number of rows for the triangle. The triangle can be upward or
# downward.
#
# Example:
# Enter the number of rows for the triangle: 5
# Enter 'u' for upward or 'd' for downward: u
#
# *
# **
# ***
# ****
# *****

rows = int(input('Enter the number of rows for the triangle: '))
up_or_down = input('Enter "u" for upward or "d" for downward: ')

if up_or_down == 'u':
    for i in range(1, rows + 1):
        print(i * '*', end = '\n')
elif up_or_down == 'd':
    for i in range(rows, 0, -1):
        print(i * '*', end='\n')
else:
    print('Invalid input!')