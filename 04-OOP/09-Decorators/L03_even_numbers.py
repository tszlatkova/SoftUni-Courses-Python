def even_numbers(function):

    def wrapper(*args, **kwargs):

        nums = function(*args, **kwargs)
        result = [el for el in nums if el % 2 == 0]
        return result

    return wrapper


# Test code 1
@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
