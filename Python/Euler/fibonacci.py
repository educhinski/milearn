"""Finds fibonacci numbers below a certain given value."""


def fibonacci(end, start=0):
    """
    Returns a list of fibonacci numbers below end_range
    starting from start_values.

    Variables:
    end_range: <int> Value which the fibonacci sequence should not exceed
    start: <int> (optional) Value to specify where sequence should start.
        default: 0
    """

    if type(end) not in [int] or type(start) not in [int]:
        raise TypeError("The end or start must be a non-negative real number")

    if end < 1:
        raise ValueError("The end value must be greater than 1")

    if start < 0:
        raise ValueError("The start value must be greater than 0")

    a, b = start, start + 1
    if end == start:
        raise ValueError("The start and end cannot be equal!")

    if end < b:
        raise ValueError("End value must be greater than the start value")

    fib_list = []
    fib_list.extend([a, b])

    # loop through the fibonacci sequence while less than end_range
    while b < end:
        a, b = b, a+b
        if b > end:
            break
        fib_list.append(b)

    return fib_list
