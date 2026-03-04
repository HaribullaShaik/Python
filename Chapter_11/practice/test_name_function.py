from name_function import get_username

def test_get_username():
    """Test the get_username function with various inputs."""
    formatted_name = get_username("John", "Doe")
    assert formatted_name == "John Doe"
def test_get_username_with_middle_name():
    """Test the get_username function with a middle name."""
    formatted_name = get_username("John", "Doe", "Michael")
    assert formatted_name == "John Michael Doe"