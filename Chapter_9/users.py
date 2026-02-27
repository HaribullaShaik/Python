# Date: 02-27-2026
class User:
    """A class representing a user."""
    def __init__(self, first_name, last_name, email):
        """Initialize the user with a first name, last name, and email."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        """Print a description of the user."""
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

user_1 = User("John", "Doe", "john.doe@example.com")
user_2 = User("Jane", "Smith", "jane.smith@example.com")
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()