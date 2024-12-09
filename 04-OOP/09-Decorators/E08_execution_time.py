# Import the time module. Create a decorator called exec_time. It should calculate how
# much time a function needs to be executed. See the examples for more clarification.
import time


def exec_time(function):

    def wrapper(*args, **kwargs):
        start = time.time()  # the current time
        function(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper


# Test code 1
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


# Test code 2
@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


# Test code 3
@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1

        
print(loop())
