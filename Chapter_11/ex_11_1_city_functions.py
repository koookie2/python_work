def city_country(city, country, population=None):
    """Return a formatted city name in the form of CITY, COUNTRY."""
    if population:
        city_name = f"{city.title()} {country.title()} - population {population}"
    else:
        city_name = f"{city.title()} {country.title()}"
    return city_name