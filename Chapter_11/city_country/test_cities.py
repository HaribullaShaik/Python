from city_country_function import get_city_country

def test_get_city_country():
    """Test the get_city_country function with various inputs."""
    formatted_location = get_city_country("santiago", "chile")
    assert formatted_location == "Santiago, Chile"

def test_get_city_country_population():
    """Test the get_city_country function with population input."""
    formatted_location = get_city_country("santiago", "chile", population=5000000)
    assert formatted_location == "Santiago, Chile - Population: 5000000"