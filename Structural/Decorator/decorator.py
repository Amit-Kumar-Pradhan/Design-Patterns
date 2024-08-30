from functools import wraps

def make_blink(function):
    """ Defines the decorator """

    # """ This make the decorator transparent in terms of its name and docstring"""
    @wraps(function)

    # Define the inner function 
    def decorator():
        #  Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply decorator here
@make_blink
def hellow_world():
    """ Original Function """
    return "Hello World!"

# Check the result of decorating
print(hellow_world())

# Check if the function name is still the same of the function being decorated
print(hellow_world.__name__)

# Check the doc string of the function still the same
print(hellow_world.__doc__)