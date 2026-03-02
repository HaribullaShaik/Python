# Date: 02-27-2026
class User:
    """A class representing a user."""
    def __init__(self, first_name, last_name, email):
        """Initialize the user with a first name, last name, and email."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0
    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Reset the number of login attempts to zero."""
        self.login_attempts = 0

    def describe_user(self):
        """Print a description of the user."""
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}, Login Attempts: {self.login_attempts}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

user_1 = User("John", "Doe", "john.doe@example.com")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login attempts after reset: {user_1.login_attempts}")
