"""t-shirt"""


def make_shirt(size, message):
    """Displays a shirt's size and the message on it"""

    print("This is a " + size + "-sized t-shirt with the " +
          "following message: \n\t\"" + message + "\"\n")


# call using positional arguments
make_shirt('small', 'My Small Tshirt')

# call using keyword arguments
make_shirt(message='Biggie Here!!!', size='Extra-Large')
