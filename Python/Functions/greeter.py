"""a function that greets the user"""


# passing info to a function
def greet_user(username):
    """Display a simple greeting to the user passed."""

    # greets the user by their name, capitalized
    print("Hello, " + username.title() + "!")


# now we pass the username to the function
greet_user('jesse')
