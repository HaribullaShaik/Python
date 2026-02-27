# Date: 02-27-2026
class Resturant:
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number
    def increment_number_served(self, additional_customers):
        """Increment the number of customers that have been served."""
        self.number_served += additional_customers

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

restaurant = Resturant("Pasta Palace", "Italian")
restaurant.describe_restaurant()
restaurant.set_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")
restaurant.increment_number_served(20)
print(f"Number of customers served in one day of business: {restaurant.number_served}")