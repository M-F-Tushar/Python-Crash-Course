# Create three different instances from the Restaurant class and call describe_restaurant() for each

class Restaurant:
    """A class representing a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print restaurant information."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Print message that restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Central", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()