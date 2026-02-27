class Resturant:
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

restaurant_1 = Resturant("Pasta Palace", "Italian")
restaurant_2 = Resturant("Burger Barn", "American")
restaurant_3 = Resturant("Sushi Spot", "Japanese")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()