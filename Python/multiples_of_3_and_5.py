# Find numbers that are multiples of 3 and 5 and finds their sum

my_multiples = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
sum_multiples = sum(my_multiples)


# use a function
def sum_multiples(range_max, multiples):
    """
    Accepts a max range(int) and list of multiples.
    Returns the sum of all the multiples in the given range.
    """
    if type(range_max) not in [int, float]:
        raise TypeError("The max range must be a non-negative real number.")

    if range_max < 0:
        raise ValueError("The max range cannot be negative.")

    multiples_set = {item for item in range(1, int(range_max))
                     for mul in multiples if item % mul == 0}

    return sum(multiples_set)
