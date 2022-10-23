# Nota that add_nums here can add two numbers but...it does not have a defaults.
# If you call add_nums(5), it will not set a default for the other parameters, and 
#  the call will fail.
#
# The add_defaults can fix that:
# It accepts a reference to a function (that should get 2 parameters), and returns 
#   a better function, one that has defults and THEN calls the original one.
#


def add_defaults(two_params_func):
    def two_params_with_defaults_func(a=0, b=0):
        return two_params_func(a,b)
    return two_params_with_defaults_func

# The following decorator actually calls add_defaults, just the same:

@add_defaults
def add_nums(a,b):
    return a+b

print(add_nums(5,7))
print(add_nums(7))
print(add_nums())