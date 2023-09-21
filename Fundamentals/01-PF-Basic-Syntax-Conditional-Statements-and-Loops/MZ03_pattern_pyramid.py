# Draw a Pyramid: The user should specify the number of rows for the pyramid. Example:
# Enter the number of rows for the pyramid: 4
#
#     *
#    ***
#   *****
#  *******

rows = int(input('Enter the number of rows for the pyramid: '))

for i in range(1, rows + 1):
    empty_space = (rows - i) * ' '
    stars = (i * 2 - 1) * '*'
    print(empty_space + stars + empty_space, end = '\n')