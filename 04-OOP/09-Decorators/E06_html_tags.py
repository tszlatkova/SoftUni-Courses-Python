# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the
# result of a function with the given tag, and return the new result. For more
# clarification, see the examples below

def tags(tag):

    def decorator(function):

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper

    return decorator


# Test code 1

@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


# Test code 2

@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
