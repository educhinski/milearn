"""a function describing pet's name and type"""


# default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# can opt to omit info if is default
describe_pet(pet_name='willie')

# this also works similarly
describe_pet('willie')

# the optional parameter can be altered, ignoring the default value
# NB: the default values have to come last, after positional arguments
describe_pet('harry', animal_type='hamster')

# or better still, will still work
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
