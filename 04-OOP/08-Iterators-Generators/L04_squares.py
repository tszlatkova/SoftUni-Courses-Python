# Create a generator function called squares that should receive a number n. It should
# generate the squares of all numbers from 1 to n (inclusive).

def squares(n):

    num = 1
    while num <= n:
        yield num ** 2
        num += 1


# Test code
print(list(squares(5)))
