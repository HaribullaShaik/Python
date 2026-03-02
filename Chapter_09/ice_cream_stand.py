# Date: 02-28-2026
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

class IceCreamStand(Resturant):
    """A class representing an ice cream stand, which is a specific type of restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the ice cream stand with a name and a default cuisine type."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        """Add a flavor to the list of available flavors."""
        self.flavors.append(flavor)

    def display_flavors(self):
        """Print the list of available flavors."""
        print(f"{self.name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()