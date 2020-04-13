"""large_shirts: advanced make_shirt function"""


# advanced make_shirt function with default values
def make_shirt(size='Large', message='I love Python'):
    """Displays a shirt's size and the message on it"""

    print("\nThis is a " + size + "-sized t-shirt with the " +
          "following message: \n\t\"" + message + "\"")


# large shirt with default message
make_shirt()

# medium shirt with default message
make_shirt('medium')

# shirt of any size with different message
make_shirt('XXL', 'Es Grande?')
