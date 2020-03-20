# Find numbers that are multiples of 3 and 5 and finds their sum

multiples = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
sum_multiples = sum(multiples)


# use a function
def sum_multiples(range_max, multiples):
    """
    Accepts a max range(int) and list of multiples.
    Returns the sum of all the multiples in the given range.
    """
    multiples_list = list({item for item in range(1, range_max)
                           for mul in multiples if item % mul == 0})

    return sum(multiples_list)
