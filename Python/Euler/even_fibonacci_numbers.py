"""Finds fibonacci numbers below a certain given value."""

a, b = 1, 2


def fibonacci(end_range, start_values=(1, 2)):
    """
    Returns a list of fibonacci numbers below end_range
    starting from start_values.

    Variables:
    end_range: Value which the fibonacci sequence should not exceed
        Ex. end_range=10 returns [1, 2, 3, 5, 8]
    start_values: default = (1, 2)
        tuple to specify beginning of sequence
    """

    fib_list = []
    a, b = start_values[0], start_values[1]
    fib_list.extend([a, b])

    # loop through the fibonacci sequence while less than end_range
    while fib_list[-1] < end_range:
        a, b = b, a+b
        if b > end_range:
            break
        fib_list.append(b)

    return fib_list


print(fibonacci(100))
