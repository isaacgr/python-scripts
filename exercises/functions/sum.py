"""Takes number and returns the sum"""


def sum_digits(*args):
    """Sum digits and raise exception if not a number"""
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError('Arguments must be of type int or float')
        total += arg
    return total
