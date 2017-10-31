"""Takes values and returns the product"""


def multiply(*args):
    """Return product of all input arguments"""
    total = 1
    for arg in args:
        if not isinstance(arg, (int, float)):
            continue
        total *= arg
    return total
