# Complete Guide to Object-Oriented Programming in Python

## Chapter Overview
Object-oriented programming (OOP) is one of the most effective approaches to writing software. In OOP, you write classes that represent real-world things and situations, and you create objects based on these classes. This chapter covers all aspects of OOP in Python from basic concepts to advanced techniques.

---

## 1. Introduction to Object-Oriented Programming

### Key Concepts
- **Class**: A blueprint that defines the general behavior of a whole category of objects
- **Object/Instance**: A specific item created from a class
- **Instantiation**: The process of making an object from a class
- **Attributes**: Variables that store information about an object
- **Methods**: Functions that belong to a class and define what objects can do

### Benefits of OOP
- Models real-world situations effectively
- Makes code more organized and reusable
- Facilitates collaboration between programmers
- Enables logical thinking and problem-solving
- Simplifies complex programming challenges

---

## 2. Creating and Using Classes

### 2.1 Basic Class Structure

#### Creating the Dog Class Example
```python
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

#### Key Components Explained:

**1. Class Definition**
- `class Dog:` - Defines a new class named Dog
- Class names use CamelCase convention
- No parentheses because we're creating from scratch

**2. Docstring**
- `"""A simple attempt to model a dog."""` - Describes what the class does
- Should be included immediately after class definition

**3. The `__init__()` Method**
- Special method that Python runs automatically when creating new instances
- Has double underscores before and after the name
- `self` parameter is required and must come first
- Initializes attributes that will be available to all methods in the class

**4. Attributes**
- `self.name = name` - Creates an attribute accessible throughout the class
- Variables prefixed with `self` are available to every method
- Attributes store information about each instance

**5. Methods**
- `sit()` and `roll_over()` are regular methods
- Only require `self` parameter since they don't need additional information
- Define behaviors that instances can perform

### 2.2 Making Instances from Classes

#### Creating and Using Dog Instances
```python
# Create an instance
my_dog = Dog('Willie', 6)

# Access attributes using dot notation
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Call methods using dot notation
my_dog.sit()
my_dog.roll_over()
```

**Output:**
```
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.
Willie rolled over!
```

#### Creating Multiple Instances
```python
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

**Output:**
```
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```

### 2.3 Practice Exercises

#### Exercise 9-1: Restaurant
**Task:** Make a class called Restaurant with `restaurant_name` and `cuisine_type` attributes. Include `describe_restaurant()` and `open_restaurant()` methods.

**Solution:**
```python
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

# Create and use instance
restaurant = Restaurant("Mario's", "Italian")
print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
```

#### Exercise 9-2: Three Restaurants
**Task:** Create three different instances from the Restaurant class and call `describe_restaurant()` for each.

**Solution:**
```python
restaurant1 = Restaurant("Tony's Pizza", "Italian")
restaurant2 = Restaurant("Sakura", "Japanese")
restaurant3 = Restaurant("El Sombrero", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
```

#### Exercise 9-3: Users
**Task:** Make a User class with `first_name`, `last_name`, and other typical profile attributes. Include `describe_user()` and `greet_user()` methods.

**Solution:**
```python
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
        """Print summary of user information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        """Print personalized greeting."""
        print(f"Hello, {self.first_name}! Welcome back!")

# Create multiple users
user1 = User("John", "Smith", 25, "john@email.com", "New York")
user2 = User("Sarah", "Johnson", 30, "sarah@email.com", "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
```

---

## 3. Working with Classes and Instances

### 3.1 The Car Class Example

```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

# Create and use car instance
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

### 3.2 Setting Default Values for Attributes

In the Car class above, `odometer_reading` is set to 0 by default. This demonstrates how to initialize attributes without requiring them as parameters.

### 3.3 Modifying Attribute Values

#### Method 1: Direct Access
```python
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# Modify attribute directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### Method 2: Through a Method
```python
class Car:
    # ... previous methods ...
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Use the method
my_new_car = Car('audi', 'a4', 2019)
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

#### Method 3: Incrementing Through a Method
```python
class Car:
    # ... previous methods ...
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't decrease the odometer reading!")

# Use increment method
my_used_car = Car('subaru', 'outback', 2015)
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

### 3.4 Practice Exercises

#### Exercise 9-4: Number Served
**Task:** Add a `number_served` attribute to Restaurant class with methods to set and increment the value.

**Solution:**
```python
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
```

#### Exercise 9-5: Login Attempts
**Task:** Add login attempt tracking to User class with increment and reset methods.

**Solution:**
```python
class User:
    """A class representing a user profile."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value
    
    def describe_user(self):
        """Print summary of user information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login attempts: {self.login_attempts}")
    
    def greet_user(self):
        """Print personalized greeting."""
        print(f"Hello, {self.first_name}! Welcome back!")
    
    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

# Test the class
user = User("John", "Smith", 25, "john@email.com", "New York")

# Increment login attempts
for i in range(5):
    user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

# Reset attempts
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
```

---

## 4. Inheritance

### 4.1 Understanding Inheritance

Inheritance allows you to create a new class based on an existing class. The new class inherits all attributes and methods from the original class but can also define new attributes and methods specific to itself.

**Key Terms:**
- **Parent Class (Superclass)**: The original class being inherited from
- **Child Class (Subclass)**: The new class that inherits from the parent

### 4.2 The `__init__()` Method for a Child Class

#### ElectricCar Example
```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):  # Inherits from Car
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)  # Call parent's __init__

# Test inheritance
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
```

**Key Points:**
- `super()` function calls methods from the parent class
- Child class automatically has access to all parent class methods
- `super().__init__()` initializes the parent class attributes

### 4.3 Defining Attributes and Methods for Child Classes

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  # New attribute specific to electric cars
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Test new functionality
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### 4.4 Overriding Methods from the Parent Class

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# If Car class had a fill_gas_tank() method, this would override it
```

### 4.5 Instances as Attributes

Sometimes you'll want to break a large class into smaller classes that work together. You can use instances of one class as attributes in another class.

```python
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 200  # Default range
        
        print(f"This car can go about {range_miles} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Create Battery instance as attribute

# Using the Battery instance
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### 4.6 Practice Exercises

#### Exercise 9-6: Ice Cream Stand
**Task:** Create IceCreamStand class that inherits from Restaurant.

**Solution:**
```python
class IceCreamStand(Restaurant):
    """A specialized restaurant for ice cream."""
    
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initialize ice cream stand attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint chip']
    
    def show_flavors(self):
        """Display available ice cream flavors."""
        print(f"\n{self.restaurant_name} has the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Test the ice cream stand
ice_cream_shop = IceCreamStand("Sweet Treats")
ice_cream_shop.describe_restaurant()
ice_cream_shop.show_flavors()
```

#### Exercise 9-7: Admin
**Task:** Create Admin class that inherits from User with privileges.

**Solution:**
```python
class Admin(User):
    """A special kind of user with administrative privileges."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize admin attributes."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = [
            "can add post",
            "can delete post", 
            "can ban user",
            "can modify settings"
        ]
    
    def show_privileges(self):
        """Display administrator privileges."""
        print(f"\n{self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Test admin functionality
admin = Admin("Alice", "Johnson", 35, "alice@company.com", "Seattle")
admin.describe_user()
admin.show_privileges()
```

#### Exercise 9-8: Privileges
**Task:** Create separate Privileges class and use it as an attribute in Admin.

**Solution:**
```python
class Privileges:
    """A class to store administrator privileges."""
    
    def __init__(self, privileges=None):
        """Initialize privileges."""
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can modify settings"
            ]
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        """Display the privileges."""
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A special kind of user with administrative privileges."""
    
    def __init__(self, first_name, last_name, age, email, location):
        """Initialize admin attributes."""
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()  # Create Privileges instance

# Test the updated admin
admin = Admin("Bob", "Wilson", 40, "bob@company.com", "Chicago")
admin.describe_user()
admin.privileges.show_privileges()
```

#### Exercise 9-9: Battery Upgrade
**Task:** Add upgrade_battery() method to Battery class.

**Solution:**
```python
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 200
        
        print(f"This car can go about {range_miles} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrade battery to 100 kWh if it isn't already."""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh!")
        else:
            print("Battery is already at maximum capacity.")

# Test battery upgrade
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
```

---

## 5. Importing Classes

### 5.1 Importing a Single Class

**File: car.py**
```python
"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

**File: my_car.py**
```python
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

### 5.2 Storing Multiple Classes in a Module

**File: car.py (updated)**
```python
"""A set of classes used to represent gas and electric cars."""

class Car:
    # ... (Car class code as above)

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 200
        
        print(f"This car can go about {range_miles} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

**File: my_electric_car.py**
```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### 5.3 Different Import Methods

#### Importing Multiple Classes from a Module
```python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

#### Importing an Entire Module
```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

#### Importing All Classes from a Module (Not Recommended)
```python
from car import *

# This method is not recommended because:
# 1. It's unclear which classes you're using
# 2. Can cause naming conflicts
# 3. Makes debugging harder
```

### 5.4 Importing a Module into a Module

**File: car.py**
```python
"""A class that can be used to represent a car."""

class Car:
    # ... (Car class definition)
```

**File: electric_car.py**
```python
"""A set of classes that can be used to represent electric cars."""
from car import Car

class Battery:
    # ... (Battery class definition)

class ElectricCar(Car):
    # ... (ElectricCar class definition)
```

**File: my_cars.py**
```python
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

### 5.5 Using Aliases

```python
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

### 5.6 Practice Exercises

#### Exercise 9-10: Imported Restaurant
**Task:** Store Restaurant class in a module and import it.

**File: restaurant.py**
```python
"""A class representing a restaurant."""

class Restaurant:
    """A class representing a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print restaurant information."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Print message that restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, customers):
        """Set the number of customers served."""
        self.number_served = customers
    
    def increment_number_served(self, additional_customers):
        """Add to the number of customers served."""
        self.number_served += additional_customers
```

**File: test_restaurant.py**
```python
from restaurant import Restaurant

my_restaurant = Restaurant("Tony's Pizza", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
```

#### Exercise 9-11: Imported Admin
**Task:** Store User, Privileges, and Admin classes in one module and import them.

**File: user_admin.py**
```python
"""Classes for representing users and administrators."""

class User:
    """A class representing a user profile."""
    # ... (complete User class definition)

class Privileges:
    """A class to store administrator privileges."""
    # ... (complete Privileges class definition)

class Admin(User):
    """A special kind of user with administrative privileges."""
    # ... (complete Admin class definition)
```

**File: test_admin.py**
```python
from user_admin import Admin

admin = Admin("Carol", "Davis", 28, "carol@company.com", "Portland")
admin.describe_user()
admin.privileges.show_privileges()
```

#### Exercise 9-12: Multiple Modules
**Task:** Store User class in one module, Privileges and Admin in another.

**File: user.py**
```python
"""A class representing a user."""

class User:
    """A class representing a user profile."""
    # ... (User class definition)
```

**File: admin.py**
```python
"""Classes for administrator functionality."""
from user import User

class Privileges:
    """A class to store administrator privileges."""
    # ... (Privileges class definition)

class Admin(User):
    """A special kind of user with administrative privileges."""
    # ... (Admin class definition)
```

**File: test_multiple_modules.py**
```python
from admin import Admin

admin = Admin("David", "Brown", 32, "david@company.com", "Boston")
admin.describe_user()
admin.privileges.show_privileges()
```

---

## 6. The Python Standard Library

### 6.1 Introduction to the Standard Library

The Python standard library is a collection of modules included with every Python installation. These modules provide pre-written functionality for common programming tasks.

### 6.2 The `random` Module

#### Using `randint()`
```python
from random import randint

# Generate random number between 1 and 6 (inclusive)
random_number = randint(1, 6)
print(f"Random number: {random_number}")

# Simulate rolling a die multiple times
print("Rolling a die 5 times:")
for i in range(5):
    roll = randint(1, 6)
    print(f"Roll {i+1}: {roll}")
```

#### Using `choice()`
```python
from random import choice

# Choose random element from a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(f"First player: {first_up}")

# Choose random elements multiple times
print("Random player selection:")
for round_num in range(3):
    selected_player = choice(players)
    print(f"Round {round_num + 1}: {selected_player}")
```

### 6.3 Practice Exercises

#### Exercise 9-13: Dice
**Task:** Make a Die class with roll_die() method, create different sided dice.

**Solution:**
```python
from random import randint

class Die:
    """A class representing a die."""
    
    def __init__(self, sides=6):
        """Initialize die with number of sides."""
        self.sides = sides
    
    def roll_die(self):
        """Roll the die and return the result."""
        result = randint(1, self.sides)
        print(f"Rolled: {result}")
        return result

# Create and test different dice
print("6-sided die (10 rolls):")
six_sided = Die()
for i in range(10):
    six_sided.roll_die()

print("\n10-sided die (10 rolls):")
ten_sided = Die(10)
for i in range(10):
    ten_sided.roll_die()

print("\n20-sided die (10 rolls):")
twenty_sided = Die(20)
for i in range(10):
    twenty_sided.roll_die()
```

#### Exercise 9-14: Lottery
**Task:** Create a lottery system with random selection.

**Solution:**
```python
from random import choice

def create_lottery_ticket():
    """Create a lottery ticket with 4 random numbers or letters."""
    lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    
    winning_ticket = []
    for i in range(4):
        selection = choice(lottery_elements)
        winning_ticket.append(selection)
    
    return winning_ticket

# Generate winning ticket
winning_numbers = create_lottery_ticket()
print("Winning lottery ticket:")
print(f"Any ticket matching {winning_numbers} wins a prize!")
```

#### Exercise 9-15: Lottery Analysis
**Task:** Run lottery simulation to see how many attempts it takes to win.

**Solution:**
```python
from random import choice

def create_winning_ticket():
    """Create the winning lottery ticket."""
    lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    
    winning_ticket = []
    for i in range(4):
        selection = choice(lottery_elements)
        winning_ticket.append(selection)
    
    return winning_ticket

def generate_random_ticket():
    """Generate a random lottery ticket."""
    lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    
    ticket = []
    for i in range(4):
        selection = choice(lottery_elements)
        ticket.append(selection)
    
    return ticket

# Set up lottery simulation
my_ticket = [1, 2, 'A', 'B']  # My ticket
attempts = 0
won = False

print(f"My ticket: {my_ticket}")
print("Starting lottery simulation...")

# Keep playing until we win
while not won:
    attempts += 1
    current_ticket = generate_random_ticket()
    
    # Check if we won (tickets match exactly)
    if current_ticket == my_ticket:
        won = True
        print(f"\nWon after {attempts} attempts!")
        print(f"Winning ticket: {current_ticket}")
    
    # Print progress every 100000 attempts
    if attempts % 100000 == 0:
        print(f"Attempted {attempts} times...")

print(f"Total attempts needed: {attempts}")
```

#### Exercise 9-16: Python Module of the Week
**Task:** Explore Python Module of the Week (PyMOTW) website.

**Response:**
The Python Module of the Week (PyMOTW) at https://pymotw.com/ is an excellent resource for learning about Python's standard library. Here are some interesting modules to explore:

**Popular Modules to Check Out:**
- `datetime` - Working with dates and times
- `json` - Working with JSON data
- `urllib` - Internet access and URL handling
- `collections` - Specialized container datatypes
- `itertools` - Functions for efficient looping
- `pathlib` - Object-oriented filesystem paths
- `logging` - Logging facility for Python
- `unittest` - Unit testing framework

**Example exploring `collections` module:**
```python
from collections import Counter, defaultdict

# Counter - count occurrences of elements
text = "hello world"
letter_count = Counter(text)
print(f"Letter frequencies: {letter_count}")

# defaultdict - dictionary with default values
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")
```

---

## 7. Styling Classes

### 7.1 Naming Conventions

#### Class Names
- Use **CamelCase** (capitalize first letter of each word)
- No underscores between words
- Examples: `Car`, `ElectricCar`, `BankAccount`, `UserProfile`

```python
# Good class names
class Car:
    pass

class ElectricCar:
    pass

class BankAccount:
    pass

# Avoid these naming styles
class car:  # Should be Car
    pass

class electric_car:  # Should be ElectricCar
    pass
```

#### Instance and Module Names
- Use **lowercase with underscores** between words
- Examples: `my_car`, `electric_car`, `user_profile`

```python
# Good instance names
my_car = Car('toyota', 'camry', 2020)
electric_vehicle = ElectricCar('tesla', 'model 3', 2021)
user_account = BankAccount('12345', 1000)

# Module names should also use underscores
# Good: car_dealership.py, bank_account.py, user_management.py
```

### 7.2 Documentation Standards

#### Class Docstrings
```python
class Restaurant:
    """A class representing a restaurant.
    
    This class can be used to model restaurants with attributes
    like name, cuisine type, and number of customers served.
    """
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant attributes.
        
        Args:
            name (str): The name of the restaurant
            cuisine_type (str): The type of cuisine served
        """
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print information about the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")
```

#### Module Docstrings
```python
"""Classes for representing restaurants and food service businesses.

This module contains classes for modeling different types of restaurants,
including regular restaurants and specialized establishments like ice cream stands.
"""

class Restaurant:
    # ... class definition
```

### 7.3 Code Organization

#### Blank Lines
```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):  # One blank line between methods
        """Return formatted car description."""
        return f"{self.year} {self.make} {self.model}".title()
    
    def read_odometer(self):
        """Print odometer reading."""
        print(f"This car has {self.odometer_reading} miles on it.")


class ElectricCar(Car):  # Two blank lines between classes
    """Represent an electric vehicle."""
    
    def __init__(self, make, model, year):
        """Initialize electric car attributes."""
        super().__init__(make, model, year)
        self.battery_size = 75
```

#### Import Organization
```python
# Standard library imports first
import random
import datetime
from pathlib import Path

# Blank line between standard library and local imports

# Local imports second
from car import Car
from restaurant import Restaurant
```

### 7.4 Complete Styling Example

```python
"""Classes for representing vehicles and transportation.

This module provides classes for modeling different types of vehicles,
with special focus on cars and electric vehicles.
"""

import random
from datetime import datetime


class Vehicle:
    """A class representing a generic vehicle."""
    
    def __init__(self, make, model, year):
        """Initialize vehicle attributes.
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The specific model name
            year (int): The year the vehicle was manufactured
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def get_descriptive_name(self):
        """Return a formatted description of the vehicle."""
        return f"{self.year} {self.make} {self.model}".title()
    
    def read_mileage(self):
        """Display the current mileage."""
        print(f"This vehicle has {self.mileage} miles on it.")
    
    def update_mileage(self, new_mileage):
        """Update the vehicle's mileage.
        
        Args:
            new_mileage (int): The new mileage reading
        """
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("You can't roll back the mileage!")


class ElectricVehicle(Vehicle):
    """A specialized vehicle class for electric vehicles."""
    
    def __init__(self, make, model, year, battery_size=75):
        """Initialize electric vehicle attributes.
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The specific model name  
            year (int): The year the vehicle was manufactured
            battery_size (int): Battery capacity in kWh
        """
        super().__init__(make, model, year)
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Display information about the battery."""
        print(f"This vehicle has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Calculate and display the vehicle's range."""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = int(self.battery_size * 3.5)  # Rough estimate
        
        print(f"This vehicle can go about {range_miles} miles on a full charge.")
```

---

## 8. Summary and Best Practices

### 8.1 Key Concepts Mastered

By completing this chapter, you've learned how to:

1. **Create Classes**: Write blueprints for objects that model real-world things
2. **Use Attributes**: Store information specific to each instance
3. **Write Methods**: Define behaviors that objects can perform
4. **Work with `__init__()`**: Initialize objects with specific attributes
5. **Modify Attributes**: Change object properties directly or through methods
6. **Use Inheritance**: Create specialized classes based on existing ones
7. **Override Methods**: Customize inherited behavior for child classes
8. **Use Composition**: Include instances of one class as attributes in another
9. **Import Classes**: Organize code across multiple modules
10. **Follow Conventions**: Write clean, readable, and maintainable code

### 8.2 Best Practices Summary

#### Design Principles
- **Single Responsibility**: Each class should have one primary purpose
- **Inheritance**: Use it to model "is-a" relationships (ElectricCar is-a Car)
- **Composition**: Use it to model "has-a" relationships (Car has-a Engine)
- **Encapsulation**: Group related data and methods together in classes

#### Code Organization
- Keep classes focused and not too large
- Use inheritance to avoid code duplication
- Store related classes in the same module
- Import only what you need
- Use descriptive names for classes, methods, and attributes

#### Documentation
- Write clear docstrings for all classes and methods
- Include module-level documentation
- Use meaningful variable and method names
- Add comments for complex logic

### 8.3 Real-World Applications

Object-oriented programming is used extensively in:

- **Web Development**: User accounts, blog posts, products in e-commerce
- **Game Development**: Characters, items, levels, game mechanics
- **Data Analysis**: Datasets, statistical models, visualization components
- **GUI Applications**: Windows, buttons, menus, dialog boxes
- **Scientific Computing**: Experiments, measurements, simulations
- **Business Applications**: Customers, orders, inventory, employees

### 8.4 Next Steps

After mastering OOP basics, you can explore:

1. **Advanced OOP Concepts**:
   - Multiple inheritance
   - Abstract base classes
   - Property decorators
   - Class methods and static methods

2. **Design Patterns**:
   - Singleton pattern
   - Factory pattern
   - Observer pattern
   - Strategy pattern

3. **Testing**:
   - Unit testing classes
   - Mock objects
   - Test-driven development

4. **Advanced Python Features**:
   - Decorators for classes
   - Context managers
   - Metaclasses
   - Data classes

### 8.5 Practice Projects

To reinforce your understanding, try building:

1. **Library Management System**: Books, Members, Loans
2. **Bank Account Simulator**: Accounts, Transactions, Interest
3. **Student Grade Tracker**: Students, Courses, Grades, Reports
4. **Inventory Management**: Products, Categories, Suppliers, Orders
5. **Simple Game**: Player, Enemies, Weapons, Levels

Each project will help you practice different aspects of OOP and understand how classes work together to create complete applications.

---

## Conclusion

Object-oriented programming is a powerful paradigm that helps you think about problems in terms of objects and their interactions. By mastering the concepts in this chapter—classes, inheritance, composition, and proper organization—you've gained tools that will make your programs more organized, reusable, and easier to maintain.

The key to becoming proficient with OOP is practice. Start with simple classes and gradually work toward more complex systems. Don't be afraid to refactor your code as you learn better ways to organize and structure your classes.

Remember that there's often no single "right" way to model real-world situations in code. Different approaches have different trade-offs, and what matters most is that your code works correctly, is easy to understand, and can be maintained over time.

Keep practicing, keep learning, and most importantly, keep coding!
