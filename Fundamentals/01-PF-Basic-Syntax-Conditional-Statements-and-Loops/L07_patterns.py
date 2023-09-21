# Write a program that receives a number and creates the following pattern. The number represents the largest count
# of stars on one row.

number = int(input())

center = number * '*'

above = ''
under = ''

for i in range(1, number):
    stars = i * '*'
    above += stars + '\n'

for i in range(number -1, 0, -1):
    stars = i * '*'
    under += stars + '\n'

whole_figure = above + center + '\n' + under
print(whole_figure)

####### SoftUni version

# number = int(input())
#
# for i in range(1, number + 1):
#     for j in range(0,i):
#         print('*', end = '')
#     print()
#
# for i in range(number - 1, 0, -1):
#     for j in range(0, i):
#         print('*', end = '')
#     print()

