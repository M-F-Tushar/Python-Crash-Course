class Restaurant:
    """A class representing a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value
    
    def describe_restaurant(self):
        """Print restaurant information."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Print message that restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, customers):
        """Set the number of customers served."""
        if customers >= 0:
            self.number_served = customers
        else:
            print("Number of customers can't be negative!")
    
    def increment_number_served(self, additional_customers):
        """Add to the number of customers served."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Additional customers can't be negative!")

# Test the class
restaurant = Restaurant("Tony's Pizza", "Italian")
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Customers served: {restaurant.number_served}")