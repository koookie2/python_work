def describe_city(city, country='india'):
    """Displays that the city is in the country"""
    print(f"{city.title()} is in {country.title()}")

describe_city('mumbai')
describe_city('chennai')
describe_city('totonto', 'canada')