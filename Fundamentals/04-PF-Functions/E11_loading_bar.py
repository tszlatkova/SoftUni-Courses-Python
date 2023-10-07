# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder
# (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number you have
# received in the input. Print the result on the console. For more clarification, see the examples below.

# 30	30% [%%%.......]
# Still loading...
# 50	50% [%%%%%.....]
# Still loading...
# 100	100% Complete!
# [%%%%%%%%%%]

def loading_bar(number: int):
    bar = ''

    count = number // 10
    percents = '%' * count
    dots = '.' * (10 - count)

    bar = percents + dots

    return bar


percentage = int(input())

if percentage == 100:
    print(f'100% Complete!')
    print(f'[{loading_bar(percentage)}]')
else:
    print(f'{percentage}% [{loading_bar(percentage)}]')
    print(f'Still loading...')
