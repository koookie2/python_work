def city_country(city, country):
    """Returns the location of a city"""
    location = f"{city.title()}, {country.title()}"
    return location

place = city_country('mumbai', 'india')
print(place)

place = city_country('chennai', 'india')
print(place)

place = city_country('totonto', 'canada')
print(place)