from functools import wraps


def make_blink(function):
    # defining the decorator
    # making the decorator transparent in terms of its name and doc string
    @wraps(function)
    # define the inner function
    def decorator():
        # grabbing the return value of the function being decorated
        ret = function()
        # adding new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
    return decorator


# apply decorator here
@make_blink
def hello_world():
    """this is the original function"""
    return "Hello World!"


# check the result of decorating
print(hello_world())
# check if the function is still the name of the func being decorated
print(hello_world.__name__)
# check if the docstring is still the same as that of function being decorated
print(hello_world.__doc__)