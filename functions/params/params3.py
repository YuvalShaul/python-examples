

def demo_params(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# demo_params(1, 2, 3, 4, 5, 6)   # WRONG: e, f should be keyword
# demo_params(a=1, b=2, c=3, d=4, e=5, f=6)  # WRONG: a, b, MUST be positional, not keyword

demo_params(1, 2, 3, 4, e=5, f=6)  # GOOD

demo_params(1, 2, c=3, d=4, e=5, f=6)  #GOOD






