# 🐍 Python Crash Course - Comprehensive Cheat Sheet

> A complete reference guide covering all Python concepts, functionalities, and keywords used in this repository.

---

## Table of Contents

1. [Basic Syntax & Variables](#1-basic-syntax--variables)
2. [Data Types](#2-data-types)
3. [String Operations](#3-string-operations)
4. [Lists](#4-lists)
5. [Tuples](#5-tuples)
6. [Dictionaries](#6-dictionaries)
7. [Conditional Statements](#7-conditional-statements)
8. [Loops](#8-loops)
9. [User Input](#9-user-input)
10. [Functions](#10-functions)
11. [Classes & OOP](#11-classes--oop)
12. [File Operations](#12-file-operations)
13. [Exception Handling](#13-exception-handling)
14. [Testing](#14-testing)
15. [External Libraries](#15-external-libraries)
16. [Python Keywords Reference](#16-python-keywords-reference)
17. [Built-in Functions Reference](#17-built-in-functions-reference)

---

## 1. Basic Syntax & Variables

### Variable Assignment
```python
# Simple assignment
name = "ada lovelace"
age = 25
pi_value = 3.14159

# Multiple assignment
x, y, z = 0, 0, 0

# Constants (by convention, use UPPERCASE)
MAX_CONNECTIONS = 5000
```

### Comments
```python
# Single-line comment

"""
Multi-line comment
or docstring
"""
```

### Print Function
```python
print("Hello, World!")
print("Hello", "World", sep=", ")  # With separator
```

---

## 2. Data Types

### Numeric Types
```python
# Integer
count = 42

# Float
price = 19.99

# Underscore in numbers (for readability)
universe_age = 14_000_000_000

# Basic arithmetic
addition = 2 + 3
subtraction = 5 - 2
multiplication = 3 * 4
division = 10 / 3        # Returns float: 3.333...
floor_division = 10 // 3  # Returns int: 3
modulus = 10 % 3         # Returns remainder: 1
exponentiation = 2 ** 3  # Returns 8
```

### Boolean
```python
is_active = True
is_logged_in = False
```

---

## 3. String Operations

### String Methods
```python
name = "ada lovelace"

# Case conversion
name.title()     # "Ada Lovelace"
name.upper()     # "ADA LOVELACE"
name.lower()     # "ada lovelace"

# Whitespace manipulation
message = " Hello Python! "
message.strip()   # "Hello Python!"
message.rstrip()  # " Hello Python!"
message.lstrip()  # "Hello Python! "
```

### String Formatting

#### F-strings (Recommended)
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

#### Format Method
```python
message = "Hello, {}!".format(name)
```

### Special Characters
```python
# Tab
print("\tPython")

# Newline
print("Languages:\nPython\nJavaScript\nRust")

# Apostrophe in string
message = "Python's simplicity is its strength"
# or
message = 'Python\'s simplicity is its strength'
```

---

## 4. Lists

### Creating Lists
```python
# Empty list
motorcycles = []

# List with items
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
```

### Accessing Elements
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Index access (0-based)
first = bicycles[0]      # 'trek'
last = bicycles[3]       # 'specialized'

# Negative indexing (from end)
last = bicycles[-1]      # 'specialized'
second_last = bicycles[-2]  # 'redline'
```

### Modifying Lists
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# Change element
motorcycles[0] = 'ducati'

# Append to end
motorcycles.append('honda')

# Insert at position
motorcycles.insert(0, 'ducati')
```

### Removing Elements
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# Delete by index
del motorcycles[0]

# Pop last element (or from specific position)
last_owned = motorcycles.pop()      # Removes and returns last
first_owned = motorcycles.pop(0)    # Removes and returns from index 0

# Remove by value
motorcycles.remove('ducati')
```

### Organizing Lists
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Permanent sort
cars.sort()              # Ascending
cars.sort(reverse=True)  # Descending

# Temporary sort
sorted(cars)             # Returns sorted copy
sorted(cars, reverse=True)

# Reverse order
cars.reverse()

# Get length
len(cars)
```

### List Operations
```python
# Slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])    # ['charles', 'martina', 'michael']
print(players[:4])     # First 4 elements
print(players[2:])     # From index 2 to end
print(players[-3:])    # Last 3 elements

# Copying lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Creates a copy
```

### List Comprehensions
```python
# Basic syntax: [expression for item in iterable]
squares = [value**2 for value in range(1, 11)]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
```

### Range Function
```python
# Generate sequence
for value in range(1, 5):      # 1, 2, 3, 4 (excludes 5)
    print(value)

numbers = list(range(1, 6))    # [1, 2, 3, 4, 5]

# With step
even_numbers = list(range(2, 11, 2))  # [2, 4, 6, 8, 10]

# Statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)     # 0
max(digits)     # 9
sum(digits)     # 45
```

---

## 5. Tuples

### Creating and Using Tuples
```python
# Tuple (immutable list)
dimensions = (200, 50)

# Access elements
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# Single element tuple (note the comma)
my_t = (3,)

# Loop through tuple
for dimension in dimensions:
    print(dimension)

# Reassigning tuple (creating new tuple)
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)  # New tuple
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
```

---

## 6. Dictionaries

### Creating Dictionaries
```python
# Empty dictionary
alien_0 = {}

# Dictionary with data
alien_0 = {'color': 'green', 'points': 5}

# Multi-line dictionary
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 30,
    'city': 'alaska'
}
```

### Accessing Values
```python
alien_0 = {'color': 'green', 'points': 5}

# Access by key
print(alien_0['color'])    # 'green'
new_points = alien_0['points']

# Using get() method (safer)
speed = alien_0.get('speed', 'No speed assigned')
```

### Modifying Dictionaries
```python
# Add new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# Modify value
alien_0['color'] = 'yellow'

# Remove key-value pair
del alien_0['points']
```

### Looping Through Dictionaries
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Loop through all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Loop through keys
for name in favorite_languages.keys():
    print(name.title())

# Loop through keys (default behavior)
for name in favorite_languages:
    print(name.title())

# Loop through values
for language in favorite_languages.values():
    print(language.title())

# Get unique values
for language in set(favorite_languages.values()):
    print(language.title())
```

### Nesting
```python
# List of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

# Dictionary with lists
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Dictionary in dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
```

---

## 7. Conditional Statements

### Comparison Operators
```python
# Equality
car == 'bmw'    # True if equal
car != 'audi'   # True if not equal

# Case-insensitive comparison
car.lower() == 'audi'

# Numerical comparisons
age == 18
age < 21
age <= 21
age > 18
age >= 18
```

### Logical Operators
```python
# AND
age_0 >= 21 and age_1 >= 21

# OR
age_0 >= 21 or age_1 >= 21

# NOT
not (age < 21)
```

### Checking Lists
```python
# Check if value in list
'mushrooms' in requested_toppings

# Check if value not in list
'anchovies' not in requested_toppings

# Check if list is empty
if requested_toppings:  # Empty list evaluates to False
    print("List has items")
```

### If Statements
```python
# Simple if
if age >= 18:
    print("You can vote!")

# if-else
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")

# if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

# Multiple elif
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
```

---

## 8. Loops

### For Loops
```python
# Basic for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# For loop with range
for value in range(1, 5):
    print(value)

# Loop with operations
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
```

### While Loops
```python
# Basic while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# While loop with user input
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### Loop Control
```python
# Break - exit loop
while True:
    name = input("Enter name (or 'quit'): ")
    if name == 'quit':
        break
    print(f"Hello, {name}!")

# Continue - skip to next iteration
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Using flags
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### Loop with Lists
```python
# Moving items between lists
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

# Removing all instances of a value
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
```

---

## 9. User Input

### Input Function
```python
# Basic input
message = input("Tell me something: ")
print(message)

# Multi-line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

# Converting input to integer
age = input("How old are you? ")
age = int(age)  # Convert string to integer

# Modulo with user input
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

---

## 10. Functions

### Defining Functions
```python
# Simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Function with parameter
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

### Function Arguments

#### Positional Arguments
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

#### Keyword Arguments
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
```

#### Default Values
```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')  # Uses default
describe_pet('harry', 'hamster')  # Overrides default
```

### Return Values
```python
# Simple return
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')

# Optional parameters
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
```

### Passing Lists
```python
# Passing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

# Prevent function from modifying list
print_models(unprinted_designs[:], completed_models)  # Pass a copy
```

### Arbitrary Number of Arguments
```python
# *args - arbitrary positional arguments
def make_pizza(*toppings):
    """Print the list of toppings."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# **kwargs - arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
```

### Importing Functions
```python
# Import entire module
import module_name
module_name.function_name()

# Import specific function
from module_name import function_name
function_name()

# Import multiple functions
from module_name import function_0, function_1, function_2

# Import all functions (not recommended)
from module_name import *

# Using alias for function
from module_name import function_name as fn

# Using alias for module
import module_name as mn
```

---

## 11. Classes & OOP

### Defining a Class
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

### Creating Instances
```python
# Create instance
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

# Access attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Call methods
my_dog.sit()
your_dog.roll_over()
```

### Working with Classes and Instances
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
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# Modifying attribute values
my_car = Car('audi', 'a4', 2019)
my_car.odometer_reading = 23  # Direct modification
my_car.update_odometer(25)    # Through method
my_car.increment_odometer(100)
```

### Inheritance
```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

### Instances as Attributes
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
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance as attribute

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

---

## 12. File Operations

### Reading Files
```python
# Read entire file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Read line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store lines in a list
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

### Writing to Files
```python
# Write to file (overwrites existing content)
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Append to file
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

### File Modes
```python
# 'r' - read (default)
# 'w' - write (overwrites)
# 'a' - append
# 'r+' - read and write
```

---

## 13. Exception Handling

### Try-Except Blocks
```python
# Basic try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Try-except with user input
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

### Handling FileNotFoundError
```python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count words in file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

### Failing Silently
```python
# Using pass to fail silently
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass  # Do nothing, fail silently
else:
    # Count and report number of words
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

---

## 14. Testing

### Unit Testing with unittest
```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
```

### Testing a Class
```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

### Common Assert Methods
```python
# assertEqual(a, b)      - Verify that a == b
# assertNotEqual(a, b)   - Verify that a != b
# assertTrue(x)          - Verify that x is True
# assertFalse(x)         - Verify that x is False
# assertIn(item, list)   - Verify that item is in list
# assertNotIn(item, list)- Verify that item is not in list
```

---

## 15. External Libraries

### Pygame (Game Development)
```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Update screen
    pygame.display.flip()
```

### Matplotlib (Data Visualization)
```python
import matplotlib.pyplot as plt

# Simple line plot
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

# Scatter plot
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.show()
```

### Plotly (Interactive Visualizations)
```python
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create bar chart
x_values = ['A', 'B', 'C', 'D']
y_values = [4, 6, 2, 8]

data = [Bar(x=x_values, y=y_values)]
layout = Layout(title='Sample Chart')

offline.plot({'data': data, 'layout': layout})
```

### Requests (HTTP Library)
```python
import requests

# Make a GET request
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results
print(f"Total repositories: {response_dict['total_count']}")
```

### JSON Module
```python
import json

# Write JSON
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# Read JSON
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
```

---

## 16. Python Keywords Reference

### Complete Keywords List
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Keyword Usage
```python
# False, True, None
is_valid = True
result = None

# and, or, not
if x > 0 and y > 0:
    pass

# as
import numpy as np

# assert
assert len(data) > 0, "Data cannot be empty"

# async, await
async def fetch_data():
    await some_async_function()

# break, continue
for item in items:
    if item == 'stop':
        break
    if item == 'skip':
        continue

# class
class MyClass:
    pass

# def
def my_function():
    pass

# del
del my_list[0]

# elif, else, if
if condition1:
    pass
elif condition2:
    pass
else:
    pass

# except, finally, try
try:
    risky_operation()
except ValueError:
    handle_error()
finally:
    cleanup()

# for
for item in items:
    print(item)

# from, import
from math import pi

# global
global_var = 10
def modify_global():
    global global_var
    global_var = 20

# in
if 'key' in dictionary:
    pass

# is
if x is None:
    pass

# lambda
square = lambda x: x**2

# nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20

# pass
def placeholder():
    pass

# raise
raise ValueError("Invalid value")

# return
def get_value():
    return 42

# while
while condition:
    pass

# with
with open('file.txt') as f:
    content = f.read()

# yield
def generator():
    yield 1
    yield 2
```

---

## 17. Built-in Functions Reference

### Common Built-in Functions
```python
# Type conversion
int('42')           # Convert to integer
float('3.14')       # Convert to float
str(42)             # Convert to string
bool(1)             # Convert to boolean
list('abc')         # Convert to list
tuple([1, 2, 3])    # Convert to tuple
dict([('a', 1)])    # Convert to dictionary
set([1, 2, 2, 3])   # Convert to set

# Input/Output
print('Hello')      # Print to console
input('Enter: ')    # Get user input

# Math functions
abs(-42)            # Absolute value: 42
pow(2, 3)           # Power: 8
round(3.14159, 2)   # Round: 3.14
sum([1, 2, 3])      # Sum: 6
min([1, 2, 3])      # Minimum: 1
max([1, 2, 3])      # Maximum: 3

# Sequence functions
len([1, 2, 3])      # Length: 3
range(5)            # Sequence: 0,1,2,3,4
enumerate(['a', 'b'])  # Index-value pairs
sorted([3, 1, 2])   # Sort: [1, 2, 3]
reversed([1, 2, 3]) # Reverse iterator
zip([1, 2], ['a', 'b'])  # Combine sequences

# Type checking
type(42)            # Get type: <class 'int'>
isinstance(42, int) # Check type: True

# Object inspection
dir(object)         # List attributes
help(function)      # Get help
id(object)          # Get object ID

# Functional programming
map(func, iterable)     # Apply function
filter(func, iterable)  # Filter items
all([True, True])       # All true: True
any([False, True])      # Any true: True

# File operations
open('file.txt')    # Open file

# Other useful functions
chr(65)             # ASCII to char: 'A'
ord('A')            # Char to ASCII: 65
eval('2 + 2')       # Evaluate expression: 4
exec('x = 5')       # Execute code
format(3.14, '.2f') # Format: '3.14'
```

### String Methods
```python
# Case conversion
str.upper()         # Uppercase
str.lower()         # Lowercase
str.title()         # Title Case
str.capitalize()    # Capitalize first
str.swapcase()      # Swap case

# Searching
str.find('sub')     # Find substring
str.index('sub')    # Find (raises error)
str.count('sub')    # Count occurrences
str.startswith('x') # Starts with
str.endswith('x')   # Ends with

# Modification
str.replace('old', 'new')  # Replace
str.strip()         # Remove whitespace
str.lstrip()        # Remove left
str.rstrip()        # Remove right
str.split()         # Split to list
str.join(list)      # Join list

# Checking
str.isalpha()       # All alphabetic
str.isdigit()       # All digits
str.isalnum()       # Alphanumeric
str.isspace()       # All whitespace
str.islower()       # All lowercase
str.isupper()       # All uppercase
```

### List Methods
```python
list.append(x)      # Add to end
list.extend(iter)   # Add multiple
list.insert(i, x)   # Insert at index
list.remove(x)      # Remove value
list.pop(i)         # Remove and return
list.clear()        # Remove all
list.index(x)       # Find index
list.count(x)       # Count occurrences
list.sort()         # Sort in place
list.reverse()      # Reverse in place
list.copy()         # Shallow copy
```

### Dictionary Methods
```python
dict.keys()         # Get keys
dict.values()       # Get values
dict.items()        # Get key-value pairs
dict.get(key)       # Get with default
dict.pop(key)       # Remove and return
dict.popitem()      # Remove last item
dict.clear()        # Remove all
dict.update(other)  # Update with other dict
dict.setdefault(k, v)  # Set if not exists
dict.copy()         # Shallow copy
```

### Set Methods
```python
set.add(x)          # Add element
set.remove(x)       # Remove (error if not found)
set.discard(x)      # Remove (no error)
set.pop()           # Remove and return
set.clear()         # Remove all
set.union(other)    # Union
set.intersection(other)  # Intersection
set.difference(other)    # Difference
set.issubset(other)      # Check subset
set.issuperset(other)    # Check superset
```

---

## Quick Tips & Best Practices

### Code Style (PEP 8)
```python
# Use 4 spaces for indentation (not tabs)
# Maximum line length: 79 characters
# Two blank lines before top-level functions and classes
# One blank line between methods in a class
# Use lowercase with underscores for function names
# Use CamelCase for class names
# Use UPPERCASE for constants

# Good
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

# Bad
def CalculateAverage(Numbers):
    return sum(Numbers)/len(Numbers)
```

### Common Idioms
```python
# Swap variables
a, b = b, a

# Chain comparisons
if 0 < x < 10:
    pass

# Check for empty sequence
if not my_list:  # Instead of: if len(my_list) == 0:
    print("List is empty")

# Enumerate instead of range(len())
for i, value in enumerate(my_list):  # Instead of: for i in range(len(my_list)):
    print(i, value)

# Use 'in' for membership
if item in my_list:  # Instead of: if my_list.count(item) > 0:
    pass

# Dictionary get with default
value = my_dict.get('key', default_value)  # Instead of: if 'key' in my_dict:

# List comprehension
squares = [x**2 for x in range(10)]  # Instead of loop with append

# Context managers for files
with open('file.txt') as f:  # Automatically closes file
    content = f.read()
```

### Performance Tips
```python
# Use list comprehensions (faster than loops)
squares = [x**2 for x in range(1000)]

# Use join for string concatenation
result = ''.join(string_list)  # Instead of: result = ''; for s in string_list: result += s

# Use sets for membership testing
my_set = set(my_list)
if item in my_set:  # O(1) instead of O(n) for lists
    pass

# Use generators for large sequences
squares = (x**2 for x in range(1000000))  # Uses () instead of []

# Avoid repeated lookups
# Good
method = obj.method
for i in range(1000):
    method()

# Bad (slower)
for i in range(1000):
    obj.method()
```

---

## Additional Resources

### Official Documentation
- [Python.org Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)

### Style Guides
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

### Community Resources
- [Python Package Index (PyPI)](https://pypi.org/)
- [Real Python](https://realpython.com/)
- [Python Weekly](https://www.pythonweekly.com/)

---

## Repository Structure Overview

This cheat sheet covers concepts from:
- **Chapter 1**: Getting Started
- **Chapter 2**: Variables and Simple Data Types
- **Chapter 3**: Introducing Lists
- **Chapter 4**: Working With Lists
- **Chapter 5**: If Statements
- **Chapter 6**: Dictionaries
- **Chapter 7**: User Input and While Loops
- **Chapter 8**: Functions
- **Chapter 9**: Classes
- **Chapter 10**: Files and Exceptions
- **Chapter 11**: Testing Your Code
- **Chapter 12-14**: Game Development with Pygame
- **Chapter 15**: Generating Data (Visualization)
- **Chapter 16**: Downloading Data (APIs, JSON, CSV)

---

**Last Updated**: 2025-11-06  
**Based on**: Python Crash Course, 2nd Edition by Eric Matthes

---

*This cheat sheet is a comprehensive reference created by analyzing all Python source files in this repository. It's designed to be a quick reference guide for Python learners working through the Python Crash Course book.*
