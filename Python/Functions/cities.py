"""cities"""


def describe_city(city, country='kenya'):
    """Displays a statement showing the city and the country"""

    print(city.title() + " is in " + country.title())


# make three calls
describe_city('nairobi')
describe_city('london', 'united kingdom')
describe_city('california', country='usa')
