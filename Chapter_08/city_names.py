def city_country(city, country):
    """Return a string of the form 'City, Country'."""
    return f"{city.title()}, {country.title()}"
city = city_country('santiago', 'chile')
print(city)