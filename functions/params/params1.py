

def demo_params(a=4, b=9, c=8):   # parameters with DEFAULT VALUES
    print(a, b, c)

# def demo_params1(a=4, b, c):    # Wrong: parameter with default value should be last
#     print(a, b, c)


demo_params(1, 2, 3)  # 1, 2, 3 are positional arguments
demo_params(1, 2)     # same
demo_params(1)        # same

demo_params(a=7, b=3, c=9)   # These are KEYWORD arguments
demo_params(c=7, a=3, b=9)   # These are KEYWORD arguments

demo_params(4, 8)   # These are KEYWORD arguments


demo_params(5, 7, None)
demo_params(5, c=7, b=None)
