# Use loops to generate the patterns based on the user's input.
#
# Handle invalid inputs and provide error messages as needed.
#
# Continue displaying the menu until the user chooses to quit.
#
# Pattern Drawing Program
#
# Menu:
# 1. Draw a Triangle
# 2. Draw a Rectangle
# 3. Draw a Pyramid
# 4. Quit
#
# Enter your choice (1/2/3/4): 1
#
# Enter the number of rows for the triangle: 5
# Enter 'u' for upward or 'd' for downward: u
#
# *
# **
# ***
# ****
# *****
#
# Enter your choice (1/2/3/4): 2
#
# Enter the number of rows for the rectangle: 4
# Enter the number of columns for the rectangle: 6
#
# ******
# ******
# ******
# ******
#
# Enter your choice (1/2/3/4): 3
#
# Enter the number of rows for the pyramid: 4
#
#    *
#   ***
#  *****
# *******
#
# Enter your choice (1/2/3/4): 4
#
# Goodbye!

print('Pattern drawing program\n')
print('Menu:\n 1. Draw a Triangle \n 2. Draw a Rectangle \n 3. Draw a Pyramid \n 4. Quit\n')

while True:
    try:
        pattern = int(input('Enter your choice (1/2/3/4): '))
    except ValueError:
        print("Invalid value. Please enter an integer! Let's try again...")
    else:
        break

while pattern != 4:

    if pattern == 1:

        while True:
            try:
                rows = int(input('Enter the number of rows for the triangle: '))
            except ValueError:
                print("Invalid value. Please enter an integer! Let's try again...")
            else:
                break

        up_or_down = input('Enter "u" for upward or "d" for downward: ')

        while up_or_down not in ['u', 'd']:
            print('Invalid option! Please enter "u" or "d". Try again.')
            up_or_down = input('Enter "u" for upward or "d" for downward: ')

        if up_or_down == 'u':
            for i in range(1, rows + 1):
                print(i * '*', end='\n')
        elif up_or_down == 'd':
            for i in range(rows, 0, -1):
                print(i * '*', end='\n')

    elif pattern == 2:

        while True:
            try:
                rows = int(input('Enter the number of rows for the rectangle: '))
            except ValueError:
                print("Invalid value. Please enter an integer! Let's try again...")
            else:
                break

        while True:
            try:
                columns = int(input('Enter the number of columns for the rectangle: '))
            except ValueError:
                print("Invalid value. Please enter an integer! Let's try again...")
            else:
                break

        for _ in range(1, rows + 1):
            print(columns * '*', end='\n')

    elif pattern == 3:

        while True:
            try:
                rows = int(input('Enter the number of rows for the pyramid: '))
            except ValueError:
                print("Invalid value. Please enter an integer! Let's try again...")
            else:
                break

        for i in range(1, rows + 1):
            empty_space = (rows - i) * ' '
            stars = (i * 2 - 1) * '*'
            print(empty_space + stars + empty_space, end='\n')

    else:
        print('Not valid choice! You should choose from 1 to 4. Please, look at the menu and try again!')

    while True:
        try:
            pattern = int(input('Enter your choice (1/2/3/4): '))
        except ValueError:
            print("Invalid value. Please enter an integer! Let's try again...")
        else:
            break

print('Goodbye!')

# https://www.youtube.com/watch?v=bqNvkAfTvIc&ab_channel=Indently # how to make it to .exe fail