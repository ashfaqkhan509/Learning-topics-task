from functools import wraps


def uppercase_decorator(func):
    @wraps
    def wrapper(*args, **kwargs):
        result = str(func(*args, **kwargs))

        return result.upper()

    return wrapper


@uppercase_decorator
def welcome():
    return "Welcome Ashfaq"


print(welcome())
