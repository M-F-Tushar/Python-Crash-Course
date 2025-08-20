class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open now!")
        
        
restaurant = Restaurant("Mario's", "Italian")
print(f"Restaurant name: {restaurant.name}")
print(f"Cuisine type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()