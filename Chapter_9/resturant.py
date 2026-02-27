# Date: 02-27-2026
class Resturant:
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

restaurant = Resturant("Pasta Palace", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()