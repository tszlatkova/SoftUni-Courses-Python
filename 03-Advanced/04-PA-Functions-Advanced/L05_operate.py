# Write a function called operate that receives an operator ("+", "-", "*" or "/") as а
# first argument and multiple numbers (integers) as additional arguments (*args). The
# function should return the result of the operator applied to all the numbers. For more
# clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

from functools import reduce


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x+y, args)
    elif operator == '-':
        return reduce(lambda x, y: x-y, args)
    elif operator == '*':
        return reduce(lambda x, y: x*y, args)
    elif operator == '/':
        if 0 not in args:
            return reduce(lambda x, y: x/y, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

# Another solution

# mapper = {
#     "+": lambda nums: reduce(lambda x, y: x+y, nums),
#     "-": lambda nums: reduce(lambda x, y: x-y, nums),
#     "*": lambda nums: reduce(lambda x, y: x*y, nums),
#     "/": lambda nums: reduce(lambda x, y: x/y, nums),
#
# }
#
#
# def operate(operator, *args):
#     return mapper[operator](args)
