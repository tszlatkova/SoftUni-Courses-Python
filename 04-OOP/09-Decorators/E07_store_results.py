# Create a class called store_results. It should be used as a decorator and store
# information about the executed functions in a file called results.txt in the format:
# "Function {func_name} was called. Result: {func_result}"


class store_results:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as file:
            file.write(f"Function {self.function.__name__} was called. "
                       f"Result: {self.function(*args, **kwargs)}\n")

        return self.function(*args, **kwargs)


# Test code 1
@store_results
def add(a, b):
    return a + b


# Test code 2
@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
