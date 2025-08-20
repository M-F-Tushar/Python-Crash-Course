# Make a user with first_name and last_name, and other typical profile attributes. Include describe_user() and greet_user() methods.

class User:
    """A class representing a user profile."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


# Create multiple users
user1 = User("John", "Smith", 25, "john@email.com", "New York")
user2 = User("Sarah", "Johnson", 30, "sarah@email.com", "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()