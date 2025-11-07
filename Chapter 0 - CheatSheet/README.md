# Python Complete Reference Guide

## Table of Contents
1. [Variables and Data Types](#variables-and-data-types)
2. [Strings](#strings)
3. [Numbers](#numbers)
4. [Lists](#lists)
5. [Tuples](#tuples)
6. [Conditional Statements](#conditional-statements)
7. [Dictionaries](#dictionaries)
8. [User Input and While Loops](#user-input-and-while-loops)
9. [Functions](#functions)
10. [Classes and OOP](#classes-and-oop)
11. [Files and Exceptions](#files-and-exceptions)
12. [Testing](#testing)
13. [Data Visualization](#data-visualization)
14. [Game Development with Pygame](#game-development-with-pygame)

---

## 1. Variables and Data Types

### Basic Variable Assignment

**Definition:** A variable is a named container that stores data values in memory.

**Explanation:** Variables allow you to store and manipulate data throughout your program. Python is dynamically typed, meaning you don't need to declare the variable type explicitly - Python infers it from the assigned value.

**Example:**
```python
message = "Hello World"
name = 'Alice'
age = 25
price = 19.99
is_active = True
```

### Multiple Assignment

**Definition:** Assigning values to multiple variables in a single line.

**Explanation:** Python allows you to assign values to several variables simultaneously, making code more concise and readable. The number of variables on the left must match the number of values on the right.

**Example:**
```python
x, y, z = 0, 1, 2
name, age, height = "Alice", 25, 5.6
# You can also swap variables easily
a, b = 10, 20
a, b = b, a  # Now a=20, b=10
```

### Variable Naming Rules

**Definition:** Guidelines for creating valid and meaningful variable names.

**Explanation:** Python has strict rules about variable naming: must start with a letter or underscore, can contain letters, numbers, and underscores, but cannot start with numbers or contain spaces. Following conventions makes code more readable.

**Example:**
```python
# Valid names
user_name = "Bob"
_private_var = 42
userName2 = "Alice"

# Invalid names (will cause errors)
# 2name = "Error"      # Can't start with number
# user-name = "Error"  # Can't use hyphens
# user name = "Error"  # Can't have spaces
```

### Constants

**Definition:** Variables that should not change during program execution.

**Explanation:** Python doesn't have built-in constant types, but by convention, variables written in ALL_CAPS are treated as constants. This signals to other developers that the value shouldn't be modified.

**Example:**
```python
MAX_CONNECTIONS = 5000
PI = 3.14159
SPEED_OF_LIGHT = 299_792_458  # Underscores improve readability
TAX_RATE = 0.08

# Use constants instead of "magic numbers"
total = price * (1 + TAX_RATE)
```

---

## 2. Strings

### String Creation

**Definition:** Strings are sequences of characters enclosed in quotes.

**Explanation:** Strings can be created using single quotes, double quotes, or triple quotes (for multiline strings). Choose double quotes when your string contains single quotes (apostrophes) and vice versa.

**Example:**
```python
single_quote = 'Hello'
double_quote = "World"
apostrophe = "It's a beautiful day"
quote = 'She said "Hello"'
multiline = """This is a
multiline string
spanning several lines"""
```

### String Methods

**Definition:** Built-in functions that perform operations on string objects.

**Explanation:** String methods allow you to manipulate text without modifying the original string (strings are immutable). Common operations include changing case, removing whitespace, and replacing text.

**Example:**
```python
name = "ada lovelace"

# Case conversion
print(name.title())      # Ada Lovelace
print(name.upper())      # ADA LOVELACE
print(name.lower())      # ada lovelace
print(name.capitalize()) # Ada lovelace

# Whitespace removal
messy = "  hello  "
print(messy.strip())     # "hello"
print(messy.lstrip())    # "hello  "
print(messy.rstrip())    # "  hello"

# String replacement
text = "I love apples"
print(text.replace('apples', 'oranges'))  # I love oranges
```

### F-Strings (Formatted Strings)

**Definition:** A modern way to embed expressions inside string literals using `f""` syntax.

**Explanation:** F-strings (formatted string literals) allow you to insert variables and expressions directly into strings by prefixing the string with `f` and placing variables in curly braces `{}`. They're more readable and faster than older formatting methods.

**Example:**
```python
first_name = "ada"
last_name = "lovelace"
age = 36

# Basic f-string
full_name = f"{first_name} {last_name}"
print(full_name)  # ada lovelace

# With methods
message = f"Hello, {full_name.title()}!"
print(message)  # Hello, Ada Lovelace!

# With expressions
print(f"{first_name} is {age} years old and will be {age + 1} next year")

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # Price: $19.99
```

### Escape Characters

**Definition:** Special character sequences that represent characters difficult to type or display.

**Explanation:** Escape characters start with a backslash `\` and allow you to include special characters in strings, such as newlines, tabs, or quotes within quoted strings.

**Example:**
```python
# Newline
print("First line\nSecond line")

# Tab
print("Name:\tAlice")

# Quotes inside strings
print("She said \"Hello\"")
print('It\'s a nice day')

# Backslash
print("C:\\Users\\Desktop")

# Combined
print("Header\n\tItem 1\n\tItem 2")
```

### String Concatenation

**Definition:** Combining multiple strings into a single string.

**Explanation:** Strings can be joined using the `+` operator or the `+=` operator for in-place concatenation. While convenient, for many concatenations, f-strings or `.join()` method are more efficient.

**Example:**
```python
# Using +
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Using +=
message = "Hello "
message += "World"
message += "!"
print(message)  # Hello World!

# Better for multiple strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Python is awesome
```

---

## 3. Numbers

### Integer Operations

**Definition:** Mathematical operations performed on whole numbers.

**Explanation:** Python supports standard arithmetic operations on integers. Division always returns a float, while floor division returns an integer. Python 3 handles large integers automatically without overflow.

**Example:**
```python
# Basic arithmetic
print(2 + 3)       # Addition: 5
print(3 - 2)       # Subtraction: 1
print(2 * 3)       # Multiplication: 6
print(3 / 2)       # Division: 1.5 (always float)
print(3 // 2)      # Floor division: 1 (integer)
print(3 % 2)       # Modulo (remainder): 1
print(3 ** 2)      # Exponent: 9

# Underscores in large numbers (for readability)
universe_age = 14_000_000_000
print(universe_age)  # 14000000000

# Compound operations
count = 5
count += 1   # count = count + 1
count -= 2   # count = count - 2
count *= 3   # count = count * 3
count //= 2  # count = count // 2
```

### Float Operations

**Definition:** Mathematical operations on decimal (floating-point) numbers.

**Explanation:** Floats represent decimal numbers but have limited precision due to how computers store them. This can lead to small rounding errors in calculations, which is important to consider in scientific or financial applications.

**Example:**
```python
print(0.1 + 0.1)   # 0.2 (as expected)
print(0.2 + 0.1)   # 0.30000000000000004 (floating-point precision issue)
print(0.2 + 0.1 == 0.3)  # False (due to precision)

# Working with floats
price = 19.99
quantity = 3
total = price * quantity
print(total)  # 59.97

# Rounding
import math
value = 3.7
print(round(value))      # 4
print(math.floor(value)) # 3
print(math.ceil(value))  # 4
```

### Type Conversion

**Definition:** Converting data from one type to another.

**Explanation:** Type conversion (also called type casting) allows you to transform data between integers, floats, and strings. This is essential when working with user input or combining different data types.

**Example:**
```python
# String to integer
age_str = "21"
age = int(age_str)
print(age + 5)  # 26

# String to float
price_str = "3.14"
price = float(price_str)
print(price * 2)  # 6.28

# Number to string
number = 42
text = str(number)
print("The answer is " + text)  # The answer is 42

# Handling errors
try:
    invalid = int("abc")
except ValueError:
    print("Cannot convert 'abc' to integer")
```

### Order of Operations (PEMDAS)

**Definition:** The sequence in which mathematical operations are performed.

**Explanation:** Python follows the PEMDAS rule: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right). Use parentheses to make your intentions clear and override default precedence.

**Example:**
```python
# Without parentheses
result = 2 + 3 * 4
print(result)  # 14 (multiplication first)

# With parentheses
result = (2 + 3) * 4
print(result)  # 20 (addition first)

# Complex expression
result = 2 ** 3 + 10 / 2 - 1
print(result)  # 8 + 5.0 - 1 = 12.0

# Use parentheses for clarity
average = (score1 + score2 + score3) / 3
area = (length + width) * 2
```

---

## 4. Lists

### Creating Lists

**Definition:** A list is an ordered, mutable collection of items enclosed in square brackets.

**Explanation:** Lists can hold items of any type (even mixed types) and can be modified after creation. They're one of Python's most versatile data structures, perfect for storing collections of related items.

**Example:**
```python
# Empty list
my_list = []
empty = list()

# List with items
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'two', 3.0, True, [5, 6]]

# List comprehension (quick creation)
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Accessing Elements

**Definition:** Retrieving individual items from a list using index positions.

**Explanation:** Lists use zero-based indexing (first item is at index 0). Negative indices count from the end (-1 is the last item). Attempting to access an index that doesn't exist raises an IndexError.

**Example:**
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Positive indexing
print(bicycles[0])   # 'trek' (first element)
print(bicycles[1])   # 'cannondale' (second element)
print(bicycles[3])   # 'specialized' (fourth element)

# Negative indexing
print(bicycles[-1])  # 'specialized' (last element)
print(bicycles[-2])  # 'redline' (second from end)
print(bicycles[-4])  # 'trek' (fourth from end)

# Using in expressions
message = f"My first bicycle was a {bicycles[0].title()}."
```

### Modifying Lists

**Definition:** Operations that change the contents of a list.

**Explanation:** Lists are mutable, meaning you can modify their contents after creation. You can change individual elements, add new items, or remove existing ones using various methods.

**Example:**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# Change element
motorcycles[0] = 'ducati'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']

# Add elements
motorcycles.append('honda')  # Add to end
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'honda']

motorcycles.insert(0, 'kawasaki')  # Insert at position
print(motorcycles)  # ['kawasaki', 'ducati', 'yamaha', 'suzuki', 'honda']

# Remove elements
del motorcycles[0]  # Delete by index
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'honda']

popped = motorcycles.pop()  # Remove last, return value
print(popped)  # 'honda'
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']

motorcycles.remove('ducati')  # Remove by value (first occurrence)
print(motorcycles)  # ['yamaha', 'suzuki']
```

### List Operations

**Definition:** Built-in functions and methods that perform operations on entire lists.

**Explanation:** Lists have numerous built-in methods for common operations like sorting, reversing, and checking membership. Some methods modify the list in place, while others return new lists.

**Example:**
```python
# Length
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # 4

# Sorting
cars.sort()  # Sort permanently (ascending)
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)  # Sort permanently (descending)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# Temporary sorting
sorted_cars = sorted(cars)  # Returns sorted copy
print(sorted_cars)  # ['audi', 'bmw', 'subaru', 'toyota']
print(cars)  # Original unchanged

# Reverse order
cars.reverse()  # Reverse permanently
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

# Check membership
print('bmw' in cars)  # True
print('ford' not in cars)  # True
```

### List Slicing

**Definition:** Extracting a portion of a list to create a new list.

**Explanation:** Slicing uses the syntax `list[start:stop:step]` to extract elements. Start is inclusive, stop is exclusive. Omitting values uses defaults: start=0, stop=end, step=1.

**Example:**
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Basic slicing
print(players[0:3])   # ['charles', 'martina', 'michael']
print(players[1:4])   # ['martina', 'michael', 'florence']

# Omitting indices
print(players[:4])    # First 4: ['charles', 'martina', 'michael', 'florence']
print(players[2:])    # From index 2 to end: ['michael', 'florence', 'eli']
print(players[:])     # Copy entire list

# Negative indices
print(players[-3:])   # Last 3: ['michael', 'florence', 'eli']
print(players[:-2])   # All except last 2

# Step parameter
print(players[::2])   # Every 2nd: ['charles', 'michael', 'eli']
print(players[::-1])  # Reverse: ['eli', 'florence', 'michael', 'martina', 'charles']
```

### Copying Lists

**Definition:** Creating an independent duplicate of a list.

**Explanation:** Simply assigning a list to a new variable creates a reference, not a copy. Both variables point to the same list. To create an independent copy, use slicing `[:]` or the `copy()` method.

**Example:**
```python
my_foods = ['pizza', 'falafel', 'carrot cake']

# Correct way - creates new list
friend_foods = my_foods[:]
friend_foods.append('ice cream')
print(my_foods)       # ['pizza', 'falafel', 'carrot cake']
print(friend_foods)   # ['pizza', 'falafel', 'carrot cake', 'ice cream']

# Wrong way - creates reference
shared_foods = my_foods
shared_foods.append('cookies')
print(my_foods)       # ['pizza', 'falafel', 'carrot cake', 'cookies']
print(shared_foods)   # ['pizza', 'falafel', 'carrot cake', 'cookies']

# Using copy() method
another_copy = my_foods.copy()
```

### List Comprehensions

**Definition:** A concise way to create lists using a single line of code.

**Explanation:** List comprehensions provide a compact syntax to generate lists from existing iterables. The basic syntax is `[expression for item in iterable if condition]`. They're more readable and often faster than traditional loops.

**Example:**
```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [number**3 for number in range(1, 6)]
print(cubes)  # [1, 8, 27, 64, 125]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# String manipulation
names = ['alice', 'bob', 'charlie']
capitalized = [name.title() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### Looping Through Lists

**Definition:** Iterating over each item in a list to perform operations.

**Explanation:** The `for` loop allows you to execute code for each item in a list. You can access just the values, or both indices and values using `enumerate()`.

**Example:**
```python
magicians = ['alice', 'david', 'carolina']

# Basic loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Loop with index
for index, value in enumerate(magicians):
    print(f"{index}: {value}")

# Loop through slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(f"First 3 players: {player.title()}")
```

### Useful List Functions

**Definition:** Built-in Python functions that work with lists.

**Explanation:** Python provides several functions for common list operations like finding minimum, maximum, and sum of numeric lists. These functions are more efficient and readable than writing loops.

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(numbers))   # Minimum: 1
print(max(numbers))   # Maximum: 10
print(sum(numbers))   # Sum: 55

# Works with comprehensions
digits = [x for x in range(1, 11)]
print(f"Min: {min(digits)}, Max: {max(digits)}, Sum: {sum(digits)}")

# Finding in non-numeric lists
words = ['apple', 'banana', 'cherry']
print(min(words))  # 'apple' (alphabetically first)
print(max(words))  # 'cherry' (alphabetically last)
```

---

## 5. Tuples

### Creating Tuples

**Definition:** An ordered, immutable collection of items enclosed in parentheses.

**Explanation:** Tuples are similar to lists but cannot be modified after creation. They're faster than lists and used when you want to protect data from accidental changes. Parentheses are optional except for empty tuples.

**Example:**
```python
# Basic tuple
dimensions = (200, 50)
coordinates = (10, 20, 30)

# Single element tuple (comma is required!)
my_tuple = (3,)
not_a_tuple = (3)  # This is just an integer with parentheses

# Without parentheses
point = 10, 20, 30
print(type(point))  # <class 'tuple'>

# Empty tuple
empty = ()
empty2 = tuple()

# Tuple from list
numbers = tuple([1, 2, 3, 4])
```

### Accessing Tuple Elements

**Definition:** Retrieving individual items from a tuple using index positions.

**Explanation:** Tuples use the same indexing as lists (zero-based, with negative indices). You can access elements and use them in expressions, but you cannot modify them.

**Example:**
```python
dimensions = (200, 50, 100)

print(dimensions[0])   # 200 (first element)
print(dimensions[1])   # 50 (second element)
print(dimensions[-1])  # 100 (last element)

# Unpacking tuples
width, height, depth = dimensions
print(f"Width: {width}, Height: {height}, Depth: {depth}")

# Using in calculations
area = dimensions[0] * dimensions[1]
print(f"Area: {area}")
```

### Tuple Characteristics

**Definition:** Key properties that distinguish tuples from other data types.

**Explanation:** Tuples are immutable (cannot be changed), faster than lists, and ideal for data that shouldn't change. While you can't modify tuple contents, you can reassign the entire tuple variable.

**Example:**
```python
dimensions = (200, 50)

# This will cause an error (tuples are immutable):
# dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment

# But you can reassign entire tuple
dimensions = (400, 100)
print(dimensions)  # (400, 100)

# Tuples are faster (good for large data)
import timeit
list_time = timeit.timeit('[1,2,3,4,5]', number=1000000)
tuple_time = timeit.timeit('(1,2,3,4,5)', number=1000000)
print(f"List: {list_time}, Tuple: {tuple_time}")

# Tuples can be dictionary keys (lists cannot)
locations = {(0, 0): 'origin', (1, 1): 'point A'}
```

### Looping Through Tuples

**Definition:** Iterating over each item in a tuple.

**Explanation:** You can loop through tuples just like lists using `for` loops. This is useful when you need to process each element but don't need to modify the data.

**Example:**
```python
dimensions = (200, 50, 100)

# Basic loop
for dimension in dimensions:
    print(dimension)

# With enumerate
for index, value in enumerate(dimensions):
    print(f"Dimension {index}: {value}")

# Multiple tuples
coordinates = [(0, 0), (1, 1), (2, 4), (3, 9)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")
```

---

## 6. Conditional Statements

### Comparison Operators

**Definition:** Operators that compare two values and return True or False.

**Explanation:** Comparison operators evaluate relationships between values. They're fundamental to decision-making in programs, used in if statements, while loops, and filtering operations.

**Example:**
```python
age = 18
height = 180

# Equality
print(age == 18)      # True (equal to)
print(age != 18)      # False (not equal to)

# Magnitude
print(height < 200)   # True (less than)
print(height <= 180)  # True (less than or equal)
print(height > 150)   # True (greater than)
print(height >= 180)  # True (greater than or equal)

# Comparing strings (alphabetical)
print('apple' < 'banana')  # True
print('Apple' < 'apple')   # True (uppercase comes first)
```

### Logical Operators

**Definition:** Operators that combine multiple conditions (and, or, not).

**Explanation:** Logical operators allow you to create complex conditions by combining simple comparisons. `and` requires all conditions to be True, `or` requires at least one, and `not` inverts the condition.

**Example:**
```python
age = 22
height = 180

# AND - both conditions must be True
if age >= 21 and height >= 170:
    print("You can ride this attraction")

# OR - at least one condition must be True
if age >= 21 or height >= 200:
    print("You meet at least one requirement")

# NOT - inverts the condition
if not age < 18:
    print("You are an adult")

# Complex conditions with parentheses
if (age >= 18 and age < 65) or height > 190:
    print("Standard ticket pricing applies")
```

### Membership Operators

**Definition:** Operators that check if a value exists in a sequence (in, not in).

**Explanation:** Membership operators test whether a value is present in a collection like a list, tuple, or string. They return True or False and are more readable than manual searching.

**Example:**
```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']

# Check if item in list
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")

# Check if item not in list
if 'anchovies' not in requested_toppings:
    print("No anchovies!")

# Works with strings
text = "Hello, World!"
if 'World' in text:
    print("Found 'World' in text")

# Works with tuples and sets
valid_colors = ('red', 'green', 'blue')
if 'yellow' not in valid_colors:
    print("Yellow is not a valid color")
```

### If Statements

**Definition:** Conditional statements that execute code based on whether conditions are True or False.

**Explanation:** If statements allow your program to make decisions. The code inside an if block only runs when the condition is True. Use if-else for binary decisions and if-elif-else for multiple conditions.

**Example:**
```python
# Simple if
age = 19
if age >= 18:
    print("You are old enough to vote!")

# If-else (binary decision)
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you're too young to vote.")

# If-elif-else (multiple conditions)
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

### Multiple Conditions

**Definition:** Using multiple if or if-elif statements to check various conditions.

**Explanation:** Independent if statements check all conditions regardless of previous results. If-elif chains stop at the first True condition. Choose based on whether conditions are mutually exclusive.

**Example:**
```python
requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

# Independent if statements (test all conditions)
print("Checking all toppings:")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

# If-elif chain (stops at first match)
print("\nChecking pizza size:")
size = 'large'
if size == 'small':
    print("Small pizza: $10")
elif size == 'medium':
    print("Medium pizza: $15")
elif size == 'large':
    print("Large pizza: $20")
    # This won't run even if added
elif size == 'large':
    print("This never executes!")
```

### Boolean Values

**Definition:** True and False values used in conditional expressions.

**Explanation:** Boolean values represent truth. Python treats many values as True or False in boolean contexts: empty collections and zero are False, non-empty collections and non-zero numbers are True.

**Example:**
```python
# Explicit booleans
game_active = True
can_edit = False

if game_active:
    print("Game is running")

# Implicit boolean (truthiness)
requested_toppings = []
if requested_toppings:
    print("Processing toppings")
else:
    print("Please add some toppings")  # This runs

# Falsy values
if 0:
    print("Won't print")
if "":
    print("Won't print")
if []:
    print("Won't print")
if None:
    print("Won't print")

# Truthy values
if 1:
    print("Will print")
if "text":
    print("Will print")
if [1, 2]:
    print("Will print")
```

### Case-Insensitive Comparisons

**Definition:** Comparing strings without regard to uppercase or lowercase letters.

**Explanation:** Use `.lower()` or `.upper()` to convert strings to the same case before comparing. This allows comparisons to ignore capitalization differences. The original string remains unchanged.

**Example:**
```python
car = 'Audi'

# Case-sensitive comparison (False)
print(car == 'audi')  # False

# Case-insensitive comparison (True)
print(car.lower() == 'audi')  # True

# Original string unchanged
print(car)  # Still 'Audi'

# Practical use
username = 'Alice'
user_input = 'alice'
if username.lower() == user_input.lower():
    print("User found!")

# Multiple comparisons
names = ['ALICE', 'Bob', 'charlie']
search = 'bob'
if search.lower() in [name.lower() for name in names]:
    print(f"{search} is in the list")
```

---

## 7. Dictionaries

### Creating Dictionaries

**Definition:** A collection of key-value pairs where each key maps to a value.

**Explanation:** Dictionaries store data as key-value pairs, allowing fast lookup by key. Keys must be immutable (strings, numbers, tuples), but values can be any type. Dictionaries are unordered in Python 3.6+, but maintain insertion order.

**Example:**
```python
# Empty dictionary
my_dict = {}
another_empty = dict()

# Dictionary with data
alien_0 = {'color': 'green', 'points': 5}

# Multi-line format (better readability)
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

# Dictionary from list of tuples
pairs = [('name', 'Alice'), ('age', 25)]
from_tuples = dict(pairs)

# Using dict() constructor
user = dict(name='Bob', age=30, active=True)
```

### Accessing Values

**Definition:** Retrieving values from a dictionary using their keys.

**Explanation:** Access dictionary values using square brackets or the `.get()` method. Direct access raises a KeyError if the key doesn't exist, while `.get()` returns None or a default value instead.

**Example:**
```python
alien_0 = {'color': 'green', 'points': 5, 'x': 0, 'y': 25}

# Direct access (raises KeyError if key doesn't exist)
print(alien_0['color'])     # 'green'
print(alien_0['points'])    # 5

# Safe access with get() - returns None if key doesn't exist
point_value = alien_0.get('points')
print(point_value)  # 5

# Get with default value
speed = alien_0.get('speed', 'No speed value assigned')
print(speed)  # 'No speed value assigned'

# Checking if key exists before accessing
if 'speed' in alien_0:
    print(alien_0['speed'])
else:
    print("Speed not defined")
```

### Modifying Dictionaries

**Definition:** Operations that add, change, or remove key-value pairs.

**Explanation:** Dictionaries are mutable, allowing you to modify them after creation. You can add new pairs, change existing values, or remove pairs using various methods.

**Example:**
```python
alien_0 = {'color': 'green', 'points': 5}

# Add new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# Modify existing value
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0['color'])  # 'yellow'

# Remove key-value pair
del alien_0['points']
print(alien_0)  # {'color': 'yellow', 'x_position': 0, 'y_position': 25}

# Remove and return value
color = alien_0.pop('color')
print(color)  # 'yellow'

# Clear all items
alien_0.clear()
print(alien_0)  # {}
```

### Looping Through Dictionaries

**Definition:** Iterating over dictionary keys, values, or key-value pairs.

**Explanation:** Dictionaries provide methods to loop through keys (`.keys()`), values (`.values()`), or both (`.items()`). This allows you to process dictionary data systematically.

**Example:**
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Loop through key-value pairs
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

# Loop through keys only
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# Loop through keys (default behavior)
for name in favorite_languages:
    print(f"{name.title()}'s favorite language")

# Loop through keys in sorted order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Loop through values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Loop through unique values (using set)
for language in set(favorite_languages.values()):
    print(language.title())
```

### Nesting - List of Dictionaries

**Definition:** Storing multiple dictionaries inside a list.

**Explanation:** Lists can contain dictionaries, allowing you to store multiple related records. This is useful for managing collections of similar objects, like players, inventory items, or database records.

**Example:**
```python
# Create individual dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Store in a list
aliens = [alien_0, alien_1, alien_2]

# Loop through list of dictionaries
for alien in aliens:
    print(alien)

# Create many similar dictionaries
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Modify some aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
```

### Nesting - List in Dictionary

**Definition:** Storing a list as a value in a dictionary.

**Explanation:** Dictionary values can be lists, allowing you to associate multiple items with a single key. This is useful for properties that have multiple values, like pizza toppings or user permissions.

**Example:**
```python
# Pizza with list of toppings
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Access the list
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# Multiple people with favorite languages
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
```

### Nesting - Dictionary in Dictionary

**Definition:** Storing dictionaries as values in another dictionary.

**Explanation:** Dictionaries can contain other dictionaries, creating hierarchical data structures. This is useful for organizing complex data like user profiles, where each user has multiple attributes.

**Example:**
```python
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

# Loop through nested dictionaries
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Access nested values
print(users['aeinstein']['first'])  # 'albert'
print(users['mcurie']['location'])  # 'paris'
```

---

## 8. User Input and While Loops

### User Input

**Definition:** Functions that allow programs to receive data from users during execution.

**Explanation:** The `input()` function pauses program execution and waits for the user to enter text. It always returns a string, so numeric input must be converted using `int()` or `float()`.

**Example:**
```python
# Basic input
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Multi-line prompt
prompt = "If you tell us who you are, we can personalize messages.\n"
prompt += "What is your first name? "
name = input(prompt)

# Converting input to integer
age = input("How old are you? ")
age = int(age)
print(f"You are {age} years old.")

# Converting input to float
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

# Handling conversion errors
try:
    age = int(input("Enter your age: "))
    print(f"In 10 years you'll be {age + 10}")
except ValueError:
    print("Please enter a valid number!")
```

### While Loops

**Definition:** A loop that repeatedly executes code as long as a condition remains True.

**Explanation:** While loops continue running until their condition becomes False. They're useful when you don't know in advance how many iterations are needed, such as processing user input until they quit.

**Example:**
```python
# Basic while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# User-controlled loop
message = ""
while message != 'quit':
    message = input("Enter a message (or 'quit' to exit): ")
    if message != 'quit':
        print(f"You said: {message}")

# Counting loop
count = 0
while count < 10:
    count += 1
    print(f"Count: {count}")

# Infinite loop (use with caution!)
# while True:
#     response = input("Enter 'quit' to exit: ")
#     if response == 'quit':
#         break
```

### Using Flags

**Definition:** Boolean variables that control the execution of a while loop.

**Explanation:** Flags make code more readable by using descriptive variable names instead of complex conditions. They're especially useful when multiple conditions can end a loop.

**Example:**
```python
# Using a flag
active = True
while active:
    message = input("Enter a message (or 'quit' to exit): ")
    
    if message == 'quit':
        active = False
    else:
        print(message)

# Multiple conditions with flags
game_active = True
player_alive = True

while game_active and player_alive:
    action = input("What do you want to do? (attack/defend/quit): ")
    
    if action == 'quit':
        game_active = False
    elif action == 'attack':
        print("You attack the enemy!")
    elif action == 'defend':
        print("You defend yourself!")
```

### Break Statement

**Definition:** A statement that immediately exits a loop, regardless of the loop condition.

**Explanation:** The `break` statement provides a way to exit a loop early when a specific condition is met. It's often used with infinite loops (`while True`) to create exit points.

**Example:**
```python
# Using break with while True
while True:
    city = input("Enter a city name (or 'quit' to exit): ")
    
    if city == 'quit':
        break
    
    print(f"I'd love to visit {city.title()}!")

# Break in counting loop
count = 0
while count < 100:
    count += 1
    if count == 5:
        break
    print(count)
# Prints: 1, 2, 3, 4

# Search with break
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
target = 7
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}")
        break
    index += 1
```

### Continue Statement

**Definition:** A statement that skips the rest of the current iteration and moves to the next one.

**Explanation:** The `continue` statement jumps back to the loop condition, skipping any remaining code in the current iteration. It's useful for filtering or skipping specific values.

**Example:**
```python
# Skip even numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# Prints: 1, 3, 5, 7, 9

# Skip specific values
banned_users = ['andrew', 'carolina', 'david']
user = ''
while user != 'quit':
    user = input("Enter username (or 'quit'): ")
    if user in banned_users:
        print(f"Sorry, {user} is banned.")
        continue
    if user != 'quit':
        print(f"Welcome, {user}!")

# Process valid input only
while True:
    value = input("Enter a positive number (or 'quit'): ")
    if value == 'quit':
        break
    try:
        number = int(value)
        if number <= 0:
            continue
        print(f"Processing {number}...")
    except ValueError:
        continue
```

### While Loops with Lists

**Definition:** Using while loops to process and modify lists.

**Explanation:** While loops are effective for moving items between lists or removing specific values. They're particularly useful when you need to modify a list while iterating through it.

**Example:**
```python
# Moving items between lists
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Removing all instances of a value
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"Original list: {pets}")

while 'cat' in pets:
    pets.remove('cat')

print(f"After removing cats: {pets}")

# Processing until list is empty
tasks = ['email', 'coding', 'meeting', 'lunch']
while tasks:
    current_task = tasks.pop(0)
    print(f"Working on: {current_task}")
```

### Filling Dictionary with User Input

**Definition:** Using while loops to collect multiple entries from users into a dictionary.

**Explanation:** While loops combined with dictionaries allow you to build data structures from user input. This is useful for surveys, polls, or any application that collects multiple user responses.

**Example:**
```python
responses = {}
polling_active = True

while polling_active:
    # Get user input
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response
    responses[name] = response
    
    # Check if another person will respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Show poll results
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")

# Build a directory
directory = {}
while True:
    print("\nPhone Directory")
    print("1. Add contact")
    print("2. Quit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        directory[name] = phone
    elif choice == '2':
        break

print("\n--- Directory ---")
for name, phone in directory.items():
    print(f"{name}: {phone}")
```

---

## 9. Functions

### Defining Functions

**Definition:** A reusable block of code that performs a specific task.

**Explanation:** Functions are defined using the `def` keyword followed by a name and parentheses. They can accept parameters (inputs) and optionally return values. Docstrings describe what the function does.

**Example:**
```python
# Basic function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()  # Call the function

# Function with parameter
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')  # Hello, Jesse!
greet_user('sarah')  # Hello, Sarah!

# Function with multiple parameters
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

### Positional Arguments

**Definition:** Arguments that must be provided in a specific order.

**Explanation:** Positional arguments are matched to parameters based on their position in the function call. The order matters - the first argument goes to the first parameter, and so on.

**Example:**
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Order matters!
describe_pet('hamster', 'harry')
# Output: I have a hamster. My hamster's name is Harry.

describe_pet('harry', 'hamster')
# Output: I have a harry. My harry's name is Hamster. (Wrong!)

# Multiple function calls
describe_pet('dog', 'willie')
describe_pet('cat', 'mittens')
describe_pet('fish', 'nemo')
```

### Keyword Arguments

**Definition:** Arguments passed with parameter names, allowing any order.

**Explanation:** Keyword arguments specify which parameter should receive each value by name. This makes function calls more readable and order-independent, reducing errors.

**Example:**
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Order doesn't matter with keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')  # Same result

# Mix positional and keyword (positional must come first)
describe_pet('dog', pet_name='willie')

# More readable for functions with many parameters
def create_user(username, email, age, city, active=True):
    """Create a user profile."""
    pass

create_user('john', email='john@email.com', age=30, city='NYC')
```

### Default Values

**Definition:** Parameters that have predefined values if no argument is provided.

**Explanation:** Default values make parameters optional. If an argument isn't provided, the default is used. Parameters with defaults must come after parameters without defaults.

**Example:**
```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.""")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Uses default 'dog'
describe_pet('willie')

# Overrides default
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')

# Function with multiple defaults
def make_pizza(size, *toppings, crust='regular', sauce='tomato'):
    """Make a pizza with specified attributes."""
    print(f"\nMaking a {size}-inch {crust} crust pizza with {sauce} sauce")
    print("Toppings:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(12, 'pepperoni', 'mushrooms')
make_pizza(16, 'pepperoni', crust='thin', sauce='pesto')
```

### Return Values

**Definition:** Data that a function sends back to the code that called it.

**Explanation:** The `return` statement ends function execution and sends a value back to the caller. Functions can return any data type, including complex structures like dictionaries or lists.

**Example:**
```python
# Simple return
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix

# Optional parameter
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name('john', 'lee', 'hooker'))  # John Lee Hooker
print(get_formatted_name('jimi', 'hendrix'))  # Jimi Hendrix

# Returning a dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # {'first': 'jimi', 'last': 'hendrix', 'age': 27}

# Returning multiple values (tuple)
def get_coordinates():
    """Return x and y coordinates."""
    return 10, 20

x, y = get_coordinates()
print(f"x={x}, y={y}")
```

### Passing Lists

**Definition:** Sending a list as an argument to a function.

**Explanation:** When you pass a list to a function, the function receives a reference to the original list. Any modifications made inside the function affect the original list.

**Example:**
```python
def greet_users(names):
    """Print a greeting to each user."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Function that modifies the list
def add_toppings(pizza, toppings):
    """Add each topping to the pizza list."""
    for topping in toppings:
        pizza.append(topping)
    print(f"Pizza now has: {pizza}")

my_pizza = ['cheese']
available_toppings = ['mushrooms', 'peppers', 'onions']
add_toppings(my_pizza, available_toppings)
print(my_pizza)  # Original list is modified!
```

### Modifying Lists in Functions

**Definition:** Changing list contents within a function and preserving the original list.

**Explanation:** Functions can modify lists passed to them. To preserve the original, pass a copy using slice notation `list[:]`. This is important when you need both the original and modified versions.

**Example:**
```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Modifies the original lists
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(f"Unprinted: {unprinted_designs}")  # Now empty!

# To preserve original, pass a copy
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)  # Pass a copy
print(f"Original still intact: {unprinted_designs}")
```

### Arbitrary Arguments (*args)

**Definition:** Accepting an unknown number of positional arguments using *parameter_name.

**Explanation:** The `*args` syntax allows a function to accept any number of positional arguments. Python collects them into a tuple that you can iterate over or process.

**Example:**
```python
def make_pizza(*toppings):
    """Print the list of toppings requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Combining with regular parameters
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Sum function using *args
def sum_all(*numbers):
    """Return the sum of all numbers."""
    return sum(numbers)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### Mixing Positional and Arbitrary Arguments

**Definition:** Using both regular and arbitrary arguments in the same function.

**Explanation:** When combining parameter types, the order must be: regular positional, *args, keyword-only, **kwargs. Regular parameters must come before *args.

**Example:**
```python
def make_pizza(size, *toppings):
    """Summarize the pizza."""
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'peppers', 'onions', 'extra cheese')

# More complex example
def build_sandwich(bread_type, *ingredients, toasted=False):
    """Build a customized sandwich."""
    sandwich = f"{bread_type} sandwich"
    if toasted:
        sandwich = f"Toasted {sandwich}"
    print(f"\n{sandwich} with:")
    for ingredient in ingredients:
        print(f"  - {ingredient}")

build_sandwich('wheat', 'turkey', 'lettuce', 'tomato')
build_sandwich('white', 'ham', 'cheese', toasted=True)
```

### Arbitrary Keyword Arguments (**kwargs)

**Definition:** Accepting an unknown number of keyword arguments using **parameter_name.

**Explanation:** The `**kwargs` syntax collects arbitrary keyword arguments into a dictionary. This is useful when you want to accept any number of key-value pairs without defining them in advance.

**Example:**
```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
# {'location': 'princeton', 'field': 'physics', 
#  'first_name': 'albert', 'last_name': 'einstein'}

# Configuration function
def configure_app(**settings):
    """Configure application with any number of settings."""
    print("Application configuration:")
    for setting, value in settings.items():
        print(f"  {setting}: {value}")

configure_app(debug=True, port=8080, host='localhost', timeout=30)

# Combining all parameter types
def complex_function(pos1, pos2, *args, keyword1='default', **kwargs):
    """Demonstrate all parameter types."""
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Keyword: {keyword1}")
    print(f"Kwargs: {kwargs}")

complex_function(1, 2, 3, 4, keyword1='custom', extra1='a', extra2='b')
```

### Importing Functions

**Definition:** Making functions from one module available in another file.

**Explanation:** Python's import system allows you to organize code into modules and reuse functions across multiple files. There are several ways to import, each with different use cases.

**Example:**
```python
# pizza.py file:
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza:")
    for topping in toppings:
        print(f"- {topping}")

# ====================
# main.py file - Method 1: Import entire module
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'peppers')

# ====================
# Method 2: Import specific functions
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'peppers')

# ====================
# Method 3: Import with alias
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# ====================
# Method 4: Import module with alias
import pizza as p

p.make_pizza(16, 'pepperoni')

# ====================
# Method 5: Import multiple functions
from pizza import make_pizza, bake_pizza, slice_pizza

# ====================
# Method 6: Import all (NOT recommended)
from pizza import *

make_pizza(16, 'pepperoni')
```

---

## 10. Classes and OOP

### Defining a Class

**Definition:** A blueprint for creating objects that bundle data (attributes) and functionality (methods).

**Explanation:** Classes define object types with attributes (data) and methods (functions). The `__init__()` method initializes new instances. `self` refers to the instance being created and must be the first parameter in methods.

**Example:**
```python
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over."""
        print(f"{self.name} rolled over!")

# Create instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

# Access attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Call methods
my_dog.sit()
your_dog.roll_over()
```

### Setting Default Values

**Definition:** Assigning initial values to attributes in the `__init__()` method.

**Explanation:** Attributes can have default values that don't require arguments during instantiation. This simplifies object creation when certain values are typically the same initially.

**Example:**
```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
        self.fuel_level = 100  # Default value
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()  # This car has 0 miles on it.
```

### Modifying Attributes

**Definition:** Changing the values of object attributes after creation.

**Explanation:** Attributes can be modified directly, through methods, or by incrementing. Using methods provides better control and validation, following encapsulation principles.

**Example:**
```python
class Car:
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_car = Car('audi', 'a4', 2019)

# Method 1: Modify directly
my_car.odometer_reading = 23
my_car.read_odometer()  # This car has 23 miles on it.

# Method 2: Through a method (better)
my_car.update_odometer(50)
my_car.read_odometer()  # This car has 50 miles on it.

# Method 3: Increment through a method
my_car.increment_odometer(100)
my_car.read_odometer()  # This car has 150 miles on it.

# Validation in action
my_car.update_odometer(25)  # You can't roll back an odometer!
```

### Inheritance

**Definition:** Creating a new class based on an existing class, inheriting its attributes and methods.

**Explanation:** Inheritance allows child classes to reuse code from parent classes while adding or overriding functionality. The child class inherits all attributes and methods, and can define new ones or override existing ones.

**Example:**
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
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def fill_gas_tank(self):
        """Simulate filling the gas tank."""
        print("Filling gas tank!")

class ElectricCar(Car):
    """Represent aspects specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  # New attribute specific to electric cars
    
    def describe_battery(self):
        """Print a statement about the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def fill_gas_tank(self):
        """Override parent method - electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# Using the child class
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())  # Inherited method
my_tesla.describe_battery()  # New method
my_tesla.fill_gas_tank()  # Overridden method
```

### Instances as Attributes

**Definition:** Using an instance of one class as an attribute of another class.

**Explanation:** Complex objects can be composed of simpler objects. This composition approach keeps classes focused and manageable, following the principle of separation of concerns.

**Example:**
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
        
        print(f"This car can go about {range_miles} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance as attribute

# Using the composition
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrading the battery
my_tesla.battery.battery_size = 100
my_tesla.battery.get_range()
```

### Importing Classes

**Definition:** Making class definitions from one module available in another file.

**Explanation:** Classes can be organized into modules and imported as needed. This keeps code organized and promotes reusability. You can import individual classes, multiple classes, or entire modules.

**Example:**
```python
# car.py file:
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
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

# ====================
# my_car.py - Method 1: Import single class
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# ====================
# Method 2: Import multiple classes
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
my_tesla = ElectricCar('tesla', 'roadster', 2019)

# ====================
# Method 3: Import entire module
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)

# ====================
# Method 4: Import with alias
from car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
```

---

## 11. Files and Exceptions

### Reading Files - Entire File

**Definition:** Opening and reading the complete contents of a file into memory.

**Explanation:** The `with` statement automatically closes the file after the block executes, even if exceptions occur. The `read()` method returns the entire file contents as a string.

**Example:**
```python
# Reading entire file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# File automatically closed after 'with' block
# No need for file_object.close()

# Removing extra whitespace
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())  # Remove trailing whitespace

# Storing filename in variable
filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
```

### Reading Files - Line by Line

**Definition:** Processing a file one line at a time using iteration.

**Explanation:** Iterating over a file object reads one line at a time, which is memory-efficient for large files. Each line includes the newline character, which can be removed with `rstrip()`.

**Example:**
```python
filename = 'pi_digits.txt'

# Read line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # Remove trailing newline

# Process each line
with open('programming.txt') as file_object:
    for line in file_object:
        line = line.rstrip()
        if line:  # Skip empty lines
            print(line.upper())

# Count lines
with open(filename) as file_object:
    lines = 0
    for line in file_object:
        lines += 1
print(f"The file has {lines} lines.")
```

### Making List of Lines

**Definition:** Storing all lines of a file in a list using `readlines()`.

**Explanation:** The `readlines()` method reads all lines and returns them as a list. This allows you to work with the file contents after the `with` block closes, useful when you need to process the data multiple times.

**Example:**
```python
filename = 'pi_digits.txt'

# Store lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

# Work with lines after file is closed
for line in lines:
    print(line.rstrip())

# Access individual lines
print(f"\nFirst line: {lines[0].rstrip()}")
print(f"Last line: {lines[-1].rstrip()}")

# Process the list
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(f"Pi has {len(pi_string)} digits stored.")
```

### Working with File Contents

**Definition:** Manipulating and analyzing data read from files.

**Explanation:** Once file contents are read into memory, you can process them like any other string or list. This includes searching, counting, concatenating, or performing calculations.

**Example:**
```python
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# Build single string from all lines
pi_string = ''
for line in lines:
    pi_string += line.strip()

# Display first 50 digits
print(f"{pi_string[:52]}...")
print(f"Total digits: {len(pi_string)}")

# Search within the file
birthday = input("Enter your birthday (mmddyy): ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Count occurrences
digit = '7'
count = pi_string.count(digit)
print(f"The digit {digit} appears {count} times.")
```

### File Paths - Relative and Absolute

**Definition:** Specifying file locations using either relative or absolute paths.

**Explanation:** Relative paths specify locations relative to the current directory. Absolute paths specify the complete path from the root directory. Use forward slashes or raw strings to handle Windows backslashes.

**Example:**
```python
# Relative path (file in same directory)
with open('file.txt') as file_object:
    contents = file_object.read()

# Relative path (file in subdirectory)
with open('text_files/filename.txt') as file_object:
    contents = file_object.read()

# Absolute path (Linux/Mac)
file_path = '/home/user/documents/filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()

# Absolute path (Windows - use raw string or forward slashes)
file_path = r'C:\Users\username\Documents\filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()

# Or use forward slashes on Windows
file_path = 'C:/Users/username/Documents/filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()

# Using pathlib (modern approach)
from pathlib import Path

path = Path('text_files/filename.txt')
contents = path.read_text()
```

### Writing to Files

**Definition:** Creating new files or overwriting existing files with data.

**Explanation:** The 'w' mode opens a file for writing, creating it if it doesn't exist or erasing its contents if it does. Be careful - 'w' mode will delete all existing content!

**Example:**
```python
# Write mode - overwrites existing content
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Python only writes strings to files
# Convert numbers to strings first
numbers = [1, 2, 3, 4, 5]
with open('numbers.txt', 'w') as file_object:
    for number in numbers:
        file_object.write(str(number) + '\n')

# Writing multiple lines at once
lines = [
    "Python is awesome.\n",
    "I love learning new things.\n",
    "Programming is fun!\n"
]
with open('thoughts.txt', 'w') as file_object:
    file_object.writelines(lines)

# Note: write() doesn't add newlines automatically
with open('test.txt', 'w') as file_object:
    file_object.write("Line 1")
    file_object.write("Line 2")  # Will be on same line!
# File contents: "Line 1Line 2"
```

### Appending to Files

**Definition:** Adding new content to the end of an existing file.

**Explanation:** The 'a' (append) mode adds new content to the end of a file without erasing existing content. If the file doesn't exist, it's created. This is useful for logs or accumulating data.

**Example:**
```python
filename = 'programming.txt'

# Append mode - adds to end of file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Building a log file
import datetime

with open('log.txt', 'a') as file_object:
    timestamp = datetime.datetime.now()
    file_object.write(f"{timestamp}: User logged in\n")

# Append if exists, create if doesn't
with open('notes.txt', 'a') as file_object:
    note = input("Enter a note: ")
    file_object.write(note + '\n')
```

### File Modes

**Definition:** Different ways to open files for reading, writing, or both.

**Explanation:** File modes determine what operations you can perform on a file. Choose the appropriate mode based on whether you need to read, write, or both, and whether you want to preserve existing content.

**Example:**
```python
# 'r' - Read (default) - file must exist
with open('file.txt', 'r') as f:
    contents = f.read()

# 'w' - Write - creates file or overwrites
with open('file.txt', 'w') as f:
    f.write("New content")

# 'a' - Append - creates file or adds to end
with open('file.txt', 'a') as f:
    f.write("Additional content")

# 'r+' - Read and write - file must exist
with open('file.txt', 'r+') as f:
    contents = f.read()
    f.write("More content")

# 'w+' - Write and read - creates or overwrites
with open('file.txt', 'w+') as f:
    f.write("Content")
    f.seek(0)  # Go back to start
    contents = f.read()

# 'a+' - Append and read
with open('file.txt', 'a+') as f:
    f.write("New line\n")
    f.seek(0)
    contents = f.read()

# Binary modes (add 'b')
with open('image.jpg', 'rb') as f:  # Read binary
    image_data = f.read()

with open('copy.jpg', 'wb') as f:  # Write binary
    f.write(image_data)
```

### Exceptions - try-except Block

**Definition:** Handling errors gracefully to prevent program crashes.

**Explanation:** The try-except block allows your program to handle errors without crashing. Code that might cause errors goes in the `try` block, and error handling goes in the `except` block.

**Example:**
```python
# Basic exception handling
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Handling user input errors
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

# Multiple operations in try block
try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    result = num1 / num2
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
```

### try-except-else Block

**Definition:** Adding code that runs only if no exceptions occurred.

**Explanation:** The `else` block runs only if the `try` block succeeds without exceptions. This separates error-prone code from code that depends on success, making the logic clearer.

**Example:**
```python
print("Give me two numbers, and I'll divide them.")

while True:
    first_number = input("\nFirst number (or 'q' to quit): ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print("Please enter numbers, not text!")
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(f"Result: {answer}")

# File processing with else
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # File was successfully opened and read
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

### Handling FileNotFoundError

**Definition:** Gracefully handling situations where files don't exist.

**Explanation:** Attempting to open a non-existent file raises a FileNotFoundError. Catching this exception allows your program to inform the user appropriately instead of crashing.

**Example:**
```python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    # Count words
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# Processing multiple files
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, '{filename}' not found.")
    else:
        words = contents.split()
        print(f"{filename}: approximately {len(words)} words")
```

### Failing Silently (pass)

**Definition:** Catching exceptions without displaying error messages.

**Explanation:** The `pass` statement does nothing, allowing exceptions to fail silently. Use this when errors are expected and acceptable, but be cautious - it can hide important problems.

**Example:**
```python
# Fail silently when file doesn't exist
try:
    with open('missing_file.txt') as f:
        contents = f.read()
except FileNotFoundError:
    pass  # Do nothing if file doesn't exist

# Counting words, ignoring missing files
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # Skip this file
    else:
        words = contents.split()
        print(f"{filename}: {len(words)} words")

# Warning: Use pass carefully!
# This hides ALL errors, which might be bad
try:
    risky_operation()
except:
    pass  # Dangerous - catches everything!

# Better: Be specific about what to ignore
try:
    risky_operation()
except SpecificError:
    pass  # Only ignore this specific error
```

### Multiple Exceptions

**Definition:** Handling different types of exceptions with separate except blocks.

**Explanation:** You can have multiple except blocks to handle different error types differently. Arrange them from most specific to most general, and use a general Exception catch-all as the last resort.

**Example:**
```python
# Multiple specific exceptions
try:
    with open('data.txt') as f:
        data = f.read()
    number = int(data)
    result = 100 / number
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File doesn't contain a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")

# Catching multiple exceptions with one except
try:
    # Some code
    pass
except (ValueError, TypeError, KeyError):
    print("One of several errors occurred!")

# General exception handler (use cautiously)
try:
    # Complex operation
    process_data()
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid value!")
except Exception as e:
    # Catches any other exception
    print(f"An unexpected error occurred: {e}")

# Getting error details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
```

### JSON Files - Storing Data

**Definition:** Saving Python data structures to JSON format files.

**Explanation:** JSON (JavaScript Object Notation) is a text format for storing structured data. Python's `json.dump()` writes Python data to a JSON file, converting lists and dictionaries into JSON format automatically.

**Example:**
```python
import json

# Store a list
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

# Store a dictionary
user_dict = {
    'username': 'johndoe',
    'age': 30,
    'email': 'john@example.com',
    'favorites': ['python', 'javascript']
}

with open('user.json', 'w') as f:
    json.dump(user_dict, f, indent=4)  # indent for readability

# Store complex nested data
game_data = {
    'player': {
        'name': 'Hero',
        'level': 5,
        'inventory': ['sword', 'shield', 'potion']
    },
    'scores': [100, 250, 175]
}

with open('game.json', 'w') as f:
    json.dump(game_data, f, indent=2)
```

### JSON Files - Loading Data

**Definition:** Reading JSON files and converting them back to Python data structures.

**Explanation:** The `json.load()` function reads JSON data from a file and converts it back into Python objects (lists become lists, objects become dictionaries).

**Example:**
```python
import json

# Load a list
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)  # [2, 3, 5, 7, 11, 13]

# Load a dictionary
with open('user.json') as f:
    user_dict = json.load(f)

print(f"Welcome back, {user_dict['username']}!")

# Load and process data
with open('game.json') as f:
    game_data = json.load(f)

player_name = game_data['player']['name']
player_level = game_data['player']['level']
print(f"{player_name} is level {player_level}")

# Check if file exists before loading
import os

filename = 'data.json'
if os.path.exists(filename):
    with open(filename) as f:
        data = json.load(f)
else:
    print("File doesn't exist!")
```

### Complete Program with JSON

**Definition:** A full application that uses JSON to remember user data between sessions.

**Explanation:** This pattern combines file operations, exception handling, and JSON to create programs that remember user information. It's useful for settings, user preferences, or any persistent data.

**Example:**
```python
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# More complex example - Settings manager
class SettingsManager:
    """Manage application settings with JSON."""
    
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Load settings from file."""
        try:
            with open(self.filename) as f:
                return json.load(f)
        except FileNotFoundError:
            return self.default_settings()
    
    def default_settings(self):
        """Return default settings."""
        return {
            'theme': 'light',
            'font_size': 12,
            'auto_save': True
        }
    
    def save_settings(self):
        """Save current settings to file."""
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f, indent=4)
    
    def update_setting(self, key, value):
        """Update a setting and save."""
        self.settings[key] = value
        self.save_settings()

# Usage
settings = SettingsManager()
print(settings.settings)
settings.update_setting('theme', 'dark')
```

---

## 12. Testing

### Using unittest - Basic Structure

**Definition:** Python's built-in framework for creating and running tests.

**Explanation:** Unittest provides a structure for writing tests as methods in classes. Tests verify that functions and classes behave as expected. Each test method should test one specific aspect of behavior.

**Example:**
```python
# name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

# test_name_function.py
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

# Run: python test_name_function.py
# Output shows which tests passed/failed
```

### Common Assert Methods

**Definition:** Methods that verify expected outcomes in unit tests.

**Explanation:** Assert methods check if conditions are true. If an assertion fails, the test fails. Unittest provides many assert methods for different comparison types.

**Example:**
```python
import unittest

class TestAssertMethods(unittest.TestCase):
    """Demonstrate various assert methods."""
    
    def test_equality(self):
        """Test assertEqual and assertNotEqual."""
        self.assertEqual(3 + 2, 5)
        self.assertNotEqual(3 + 2, 6)
    
    def test_boolean(self):
        """Test assertTrue and assertFalse."""
        self.assertTrue(5 > 3)
        self.assertFalse(5 < 3)
    
    def test_membership(self):
        """Test assertIn and assertNotIn."""
        colors = ['red', 'blue', 'green']
        self.assertIn('red', colors)
        self.assertNotIn('yellow', colors)
    
    def test_comparison(self):
        """Test comparison assertions."""
        self.assertGreater(5, 3)
        self.assertLess(3, 5)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(3, 5)
    
    def test_none(self):
        """Test assertIsNone and assertIsNotNone."""
        value = None
        self.assertIsNone(value)
        self.assertIsNotNone("something")
    
    def test_type(self):
        """Test assertIsInstance."""
        self.assertIsInstance('text', str)
        self.assertIsInstance(42, int)
        self.assertIsInstance([1, 2], list)

if __name__ == '__main__':
    unittest.main()
```

### Testing a Class

**Definition:** Writing tests to verify that class methods work correctly.

**Explanation:** Class testing involves creating instances and testing their methods. Each test should be independent - changes in one test shouldn't affect others. Tests verify both expected behavior and edge cases.

**Example:**
```python
# survey.py
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

### Using setUp() Method

**Definition:** A method that runs before each test method to set up test fixtures.

**Explanation:** The `setUp()` method eliminates code duplication by creating objects needed by multiple tests. It runs automatically before each test method, ensuring each test starts with a fresh setup.

**Example:**
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
    
    def tearDown(self):
        """Clean up after each test (optional)."""
        # This runs after each test method
        # Use for cleanup like closing files, database connections, etc.
        pass

if __name__ == '__main__':
    unittest.main()

# More complex setUp example
class TestEmployee(unittest.TestCase):
    """Test the Employee class."""
    
    def setUp(self):
        """Create an employee for testing."""
        self.employee = Employee('John', 'Doe', 50000)
        self.default_raise = 5000
        self.custom_raise = 10000
    
    def test_give_default_raise(self):
        """Test default raise amount."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)
    
    def test_give_custom_raise(self):
        """Test custom raise amount."""
        self.employee.give_raise(self.custom_raise)
        self.assertEqual(self.employee.salary, 60000)
```

---

## 13. Data Visualization

### Matplotlib Basics - Installing

**Definition:** Installing the Matplotlib library for creating visualizations.

**Explanation:** Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations. Install it using pip, Python's package installer.

**Example:**
```bash
# Install matplotlib
python -m pip install --user matplotlib

# Install specific version
python -m pip install --user matplotlib==3.5.1

# Upgrade to latest version
python -m pip install --upgrade --user matplotlib

# Verify installation
python -c "import matplotlib; print(matplotlib.__version__)"
```

### Simple Line Graph

**Definition:** Creating a basic line plot to visualize data trends.

**Explanation:** Line graphs show how values change over time or across categories. Matplotlib's object-oriented interface uses `subplots()` to create figure and axes objects, providing fine control over the plot.

**Example:**
```python
import matplotlib.pyplot as plt

# Basic line plot
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()

# Corrected plot with x and y values
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()

# Multiple lines
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

fig, ax = plt.subplots()
ax.plot(x, y1, linewidth=2, label='Squares')
ax.plot(x, y2, linewidth=2, label='Linear')
ax.legend()

plt.show()
```

### Scatter Plot

**Definition:** Visualizing individual data points to show relationships or patterns.

**Explanation:** Scatter plots display individual data points without connecting them. They're ideal for showing correlations, distributions, or clusters. Color and size can encode additional information.

**Example:**
```python
import matplotlib.pyplot as plt

# Simple scatter plot
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# Scatter plot with many points
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()

# Colormap for visualization
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

### Saving Plots

**Definition:** Exporting visualizations to image files.

**Explanation:** Instead of displaying plots with `show()`, you can save them to files. The `bbox_inches='tight'` parameter trims extra whitespace around the figure.

**Example:**
```python
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Save the figure
plt.savefig('squares_plot.png', bbox_inches='tight')

# Different formats
plt.savefig('squares_plot.pdf', bbox_inches='tight')  # PDF
plt.savefig('squares_plot.svg', bbox_inches='tight')  # SVG
plt.savefig('squares_plot.jpg', bbox_inches='tight', dpi=300)  # High-res JPEG

# Save without displaying
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.savefig('output.png')
plt.close()  # Close figure to free memory
```

### Random Walks - RandomWalk Class

**Definition:** A class that generates random walk data for visualization.

**Explanation:** A random walk is a path where each step's direction and distance are chosen randomly. This class simulates random walks, useful for modeling phenomena like particle motion or stock prices.

**Example:**
```python
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)

# Using the RandomWalk class
rw = RandomWalk()
rw.fill_walk()
print(f"Number of points: {len(rw.x_values)}")
print(f"X range: {min(rw.x_values)} to {max(rw.x_values)}")
print(f"Y range: {min(rw.y_values)} to {max(rw.y_values)}")
```

### Visualizing Random Walk

**Definition:** Creating visualizations of random walk data.

**Explanation:** Random walks can be visualized as scatter plots where point colors show the order of steps. This reveals the path taken and makes patterns visible.

**Example:**
```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Create a random walk and plot the points
rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))

# Color points by their order
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
          cmap=plt.cm.Blues, edgecolors='none', s=1)

# Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
          edgecolors='none', s=100)

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

# Generate multiple random walks
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
              cmap=plt.cm.Blues, s=15)
    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
```

### Plotly - Installing

**Definition:** Installing Plotly for creating interactive visualizations.

**Explanation:** Plotly creates interactive plots that users can zoom, pan, and hover over. It's excellent for web-based visualizations and dashboards.

**Example:**
```bash
# Install plotly
python -m pip install --user plotly

# Install specific version
python -m pip install --user plotly==5.10.0

# Verify installation
python -c "import plotly; print(plotly.__version__)"
```

### Rolling Dice Simulation

**Definition:** Simulating dice rolls and visualizing the results with Plotly.

**Explanation:** Dice simulations demonstrate probability and statistics. Rolling dice many times shows that results approach the expected distribution.

**Example:**
```python
# die.py
from random import randint

class Die:
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

# rw_visual.py
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                  xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

# Rolling two dice
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 50,000 times',
                  xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
```

### Working with CSV Data

**Definition:** Reading and processing CSV (Comma-Separated Values) files.

**Explanation:** CSV files are a common format for storing tabular data. Python's `csv` module provides tools to read and parse CSV files efficiently.

**Example:**
```python
import csv

# Reading CSV
filename = 'data/sitka_weather_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Get header row
    
    print(header_row)  # See all headers
    
    # Extract specific column
    highs = []
    for row in reader:
        high = int(row[5])  # Column 5 contains high temps
        highs.append(high)

print(highs)

# Examining headers with indices
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Extracting and reading data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plotting the data
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(highs, c='red')

ax.set_title("Daily high temperatures, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

### Handling Dates

**Definition:** Parsing and working with date strings in data files.

**Explanation:** The `datetime` module allows parsing date strings and working with dates as objects. This enables proper time-series plotting and date arithmetic.

**Example:**
```python
from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Extract dates and high temperatures
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot data
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)

# Format plot
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # Draw date labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# Date format codes reference
"""
%Y  # Four-digit year (2018)
%y  # Two-digit year (18)
%m  # Month as number (01-12)
%B  # Full month name (January)
%b  # Abbreviated month name (Jan)
%d  # Day of month (01-31)
%A  # Full weekday name (Monday)
%a  # Abbreviated weekday name (Mon)
%H  # Hour 24-hour format (00-23)
%I  # Hour 12-hour format (01-12)
%p  # AM/PM
%M  # Minute (00-59)
%S  # Second (00-59)
"""

# Parsing different date formats
date_str1 = '2018-07-01'
date1 = datetime.strptime(date_str1, '%Y-%m-%d')

date_str2 = 'July 1, 2018'
date2 = datetime.strptime(date_str2, '%B %d, %Y')

date_str3 = '07/01/18'
date3 = datetime.strptime(date_str3, '%m/%d/%y')
```

### Error Checking for Missing Data

**Definition:** Handling incomplete or malformed data in CSV files.

**Explanation:** Real-world data often has missing values or errors. Use try-except blocks to skip problematic data while processing the rest successfully.

**Example:**
```python
from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Extract dates, highs, and lows
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# More robust error handling
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
        except ValueError as e:
            print(f"Error in row: {row}")
            print(f"Error message: {e}")
        except IndexError:
            print(f"Row has missing columns: {row}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
```

### Working with JSON Data

**Definition:** Loading and processing JSON data for visualization.

**Explanation:** JSON files store structured data that's easy to parse. Python's `json` module loads JSON directly into Python dictionaries and lists.

**Example:**
```python
import json

# Loading JSON data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Explore the structure
print(type(all_eq_data))  # dict
print(all_eq_data.keys())  # see top-level keys

# Access nested data
all_eq_dicts = all_eq_data['features']
print(f"Number of earthquakes: {len(all_eq_dicts)}")

# Extract specific information
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])

# Print first earthquake nicely
first_eq = all_eq_dicts[0]
print(json.dumps(first_eq, indent=4))
```

### Creating Map Visualization

**Definition:** Using Plotly to create interactive geographic visualizations.

**Explanation:** Plotly's Scattergeo creates maps where data points are positioned by latitude and longitude. Size and color can encode additional information.

**Example:**
```python
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

# Load earthquake data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

# Extract magnitudes and locations
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

# Customized map
my_layout = Layout(
    title='Global Earthquakes - Past 30 Days',
    geo=dict(
        projection=dict(type='natural earth'),
        showland=True,
        landcolor='rgb(243, 243, 243)',
        coastlinecolor='rgb(204, 204, 204)',
    )
)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_custom.html')
```

---

## 14. Game Development with Pygame

### Pygame Basics - Installing

**Definition:** Installing the Pygame library for game development.

**Explanation:** Pygame is a set of Python modules designed for writing video games. It provides functionality for graphics, sound, and game controls.

**Example:**
```bash
# Install pygame
python -m pip install --user pygame

# Install specific version
python -m pip install --user pygame==2.1.0

# Verify installation
python -c "import pygame; print(pygame.ver)"

# Test pygame installation
python -m pygame.examples.aliens
```

### Basic Game Window

**Definition:** Creating a basic game window with Pygame.

**Explanation:** A Pygame application requires initializing Pygame, creating a display surface, and running a game loop that handles events and updates the display.

**Example:**
```python
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        # Set the background color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

### Settings Class

**Definition:** A class to store all game settings in one place.

**Explanation:** Centralizing settings makes them easy to modify and keeps the main code clean. Settings include screen dimensions, colors, speeds, and other game parameters.

**Example:**
```python
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

# Using settings in main game
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
```

### Creating Game Objects - Ship Class

**Definition:** A class representing the player's ship with attributes and methods.

**Explanation:** Game objects like ships are represented as classes. They manage their own images, positions, and behaviors. The ship responds to keyboard input and stays within screen boundaries.

**Example:**
```python
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

# Using the ship in the main game
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
```

### Bullet Class (Sprite)

**Definition:** A class representing bullets as Pygame sprites.

**Explanation:** Sprites are game objects that can be grouped and managed together. Bullets inherit from Sprite to use Pygame's group functionality for efficient updating and collision detection.

**Example:**
```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

# Managing bullets in the main game
class AlienInvasion:
    def __init__(self):
        # ... other initialization ...
        self.bullets = pygame.sprite.Group()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
```

### Event Handling - Keyboard Events

**Definition:** Responding to keyboard input for game controls.

**Explanation:** Pygame's event system detects keyboard presses and releases. Separate methods for KEYDOWN and KEYUP events keep code organized and handle continuous movement smoothly.

**Example:**
```python
import sys
import pygame

class AlienInvasion:
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

# Common key constants
"""
pygame.K_LEFT         # Left arrow
pygame.K_RIGHT        # Right arrow
pygame.K_UP           # Up arrow
pygame.K_DOWN         # Down arrow
pygame.K_SPACE        # Spacebar
pygame.K_RETURN       # Enter/Return
pygame.K_ESCAPE       # Escape key
pygame.K_q            # Q key
pygame.K_a            # A key
pygame.K_w, K_s, K_a, K_d  # WASD keys
"""

# Alternative: Checking key states continuously
def _update_ship(self):
    """Update ship based on keys currently pressed."""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        self.ship.rect.x += self.settings.ship_speed
    if keys[pygame.K_LEFT]:
        self.ship.rect.x -= self.settings.ship_speed
```

### Event Handling - Mouse Events

**Definition:** Detecting and responding to mouse clicks and movement.

**Explanation:** Mouse events provide coordinates of clicks, allowing interaction with buttons and other UI elements. Check if clicks occur within button rectangles to trigger actions.

**Example:**
```python
class Button:
    """A class to build buttons for the game."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                         self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# Handling mouse clicks
class AlienInvasion:
    def __init__(self):
        # ... other initialization ...
        self.play_button = Button(self, "Play")
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Hide the mouse cursor
            pygame.mouse.set_visible(False)
```

### Sprite Groups

**Definition:** Using Pygame groups to manage collections of sprites efficiently.

**Explanation:** Groups store sprites and provide methods to update and draw all members at once. This simplifies code and improves performance for managing multiple game objects.

**Example:**
```python
import pygame

class AlienInvasion:
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        # ... screen setup ...
        
        # Create sprite groups
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update all bullets in the group
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _update_screen(self):
        """Update images on the screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # Draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draw all aliens
        self.aliens.draw(self.screen)
        
        # Draw the score information
        self.sb.show_score()
        
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

# Group methods
"""
group.add(sprite)         # Add sprite to group
group.remove(sprite)      # Remove sprite from group
group.empty()             # Remove all sprites
group.sprites()           # Return list of all sprites
group.update()            # Call update() on all sprites
group.draw(surface)       # Draw all sprites (if they have image and rect)
len(group)                # Number of sprites in group
"""
```

### Collision Detection

**Definition:** Detecting when game objects overlap or touch.

**Explanation:** Pygame provides collision detection functions that check if sprite rectangles overlap. Different functions handle sprite-to-sprite and group-to-group collisions.

**Example:**
```python
import pygame

class AlienInvasion:
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided
        # True, True means remove both bullets and aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
    
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

# Collision detection functions
"""
# Check if one sprite collides with any in a group
sprite = pygame.sprite.spritecollideany(sprite, group)

# Get all sprites in group that collide with sprite
collided = pygame.sprite.spritecollide(sprite, group, dokill)

# Check collisions between two groups
collisions = pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
# Returns dict: {sprite1: [sprite2, sprite3], ...}

# Check if two rectangles collide
rect1.colliderect(rect2)

# Check if a point is inside a rectangle
rect.collidepoint(x, y)
"""

# Custom collision with distance
import math

def check_collision(sprite1, sprite2, distance):
    """Check if two sprites are within distance of each other."""
    dx = sprite1.rect.centerx - sprite2.rect.centerx
    dy = sprite1.rect.centery - sprite2.rect.centery
    distance_between = math.sqrt(dx**2 + dy**2)
    return distance_between < distance
```

### Creating Alien Fleet

**Definition:** Calculating and creating a grid of alien sprites.

**Explanation:** The alien fleet is created by calculating how many aliens fit horizontally and vertically based on screen size and alien dimensions. Nested loops create the grid pattern.

**Example:**
```python
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                  self.settings.fleet_direction)
        self.rect.x = self.x

class AlienInvasion:
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
```

### Game Statistics

**Definition:** A class to track game statistics and state.

**Explanation:** The GameStats class manages scoring, level, lives remaining, and active state. It separates game data from game logic, making the code more organized.

**Example:**
```python
class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start game in an inactive state
        self.game_active = False
        
        # High score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

# Using statistics in the main game
class AlienInvasion:
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        # ... screen setup ...
        
        # Create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
    
    def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break
```

### Scoring System

**Definition:** Displaying and updating score, high score, and level on screen.

**Explanation:** The Scoreboard class renders text as images and positions them on screen. It updates whenever the score changes and manages the high score persistence.

**Example:**
```python
import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

# Updating scores during gameplay
class AlienInvasion:
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
```

### Dynamic Difficulty

**Definition:** Gradually increasing game difficulty as the player progresses.

**Explanation:** Dynamic difficulty adjusts game parameters like speed and scoring as levels increase. This keeps the game challenging and engaging throughout.

**Example:**
```python
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)

# Using dynamic difficulty in the game
class AlienInvasion:
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # If the entire fleet is destroyed, start a new level
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Hide the mouse cursor
            pygame.mouse.set_visible(False)
```

### Common Pygame Constants

**Definition:** Predefined values for events, keys, and colors in Pygame.

**Explanation:** Pygame provides constants for common values to make code more readable and maintainable. Use these instead of magic numbers.

**Example:**
```python
import pygame

# Event Types
"""
pygame.QUIT              # Window close button clicked
pygame.KEYDOWN           # Key pressed
pygame.KEYUP             # Key released
pygame.MOUSEBUTTONDOWN   # Mouse button clicked
pygame.MOUSEBUTTONUP     # Mouse button released
pygame.MOUSEMOTION       # Mouse moved
"""

# Key Constants
"""
# Arrow keys
pygame.K_LEFT            # Left arrow
pygame.K_RIGHT           # Right arrow
pygame.K_UP              # Up arrow
pygame.K_DOWN            # Down arrow

# Special keys
pygame.K_SPACE           # Spacebar
pygame.K_RETURN          # Enter/Return key
pygame.K_ESCAPE          # Escape key
pygame.K_BACKSPACE       # Backspace
pygame.K_TAB             # Tab
pygame.K_DELETE          # Delete

# Letter keys
pygame.K_a through pygame.K_z  # A through Z keys
pygame.K_q               # Q key
pygame.K_w               # W key (WASD for movement)

# Number keys
pygame.K_0 through pygame.K_9  # Number keys

# Function keys
pygame.K_F1 through pygame.K_F12  # Function keys

# Modifiers
pygame.KMOD_SHIFT        # Shift key modifier
pygame.KMOD_CTRL         # Ctrl key modifier
pygame.KMOD_ALT          # Alt key modifier
"""

# Colors (RGB tuples)
"""
# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Grays
LIGHT_GRAY = (230, 230, 230)
GRAY = (128, 128, 128)
DARK_GRAY = (60, 60, 60)

# Common game colors
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
"""

# Using constants in game code
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (230, 230, 230)
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.fire_weapon()
```

---

## Python Best Practices Summary

### Naming Conventions

**Definition:** Standardized rules for naming variables, functions, and classes.

**Explanation:** Following PEP 8 naming conventions makes code more readable and helps other developers understand your code. Different types of identifiers use different naming styles.

**Example:**
```python
# Variables and functions: lowercase_with_underscores (snake_case)
user_name = "Alice"
total_count = 100
def calculate_total_price():
    pass

# Classes: CapitalizedWords (PascalCase)
class MyClass:
    pass

class UserAccount:
    pass

class HTTPServerError:
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_KEY = "your_key_here"

# Private/internal: _leading_underscore
def _helper_function():
    pass

_internal_cache = {}

# Strongly private (name mangling): __double_leading
class MyClass:
    def __init__(self):
        self.__private_var = "secret"

# Module-level private: _single_leading
_module_constant = 42
```

### Code Organization

**Definition:** Structuring code for readability and maintainability.

**Explanation:** Proper organization includes import order, spacing between functions and classes, and logical grouping of related code. This makes code easier to navigate and understand.

**Example:**
```python
# Import order: standard library, third-party, local
import sys
import os
from datetime import datetime

import numpy as np
import pygame

from my_module import my_function
from my_package.submodule import MyClass


# Two blank lines before top-level functions and classes
def first_function():
    """Function docstring."""
    pass


def second_function():
    """Another function."""
    pass


class MyClass:
    """Class docstring."""
    
    def __init__(self):
        """Initialize the class."""
        pass
    
    def method_one(self):
        """First method."""
        pass
    
    def method_two(self):
        """Second method."""
        pass


class AnotherClass:
    """Another class."""
    pass


# Main execution guard
if __name__ == '__main__':
    main()
```

### Commenting Best Practices

**Definition:** Writing meaningful comments that explain why, not what.

**Explanation:** Good comments explain the reasoning behind code decisions, not the obvious mechanics. Use docstrings for functions and classes, and inline comments sparingly for complex logic.

**Example:**
```python
# Good comments - explain WHY
# Calculate tax using state rate because items ship from California
tax = amount * 0.0825

# Use binary search because list is already sorted
result = binary_search(sorted_list, target)

# Cache results to avoid expensive API calls
if key in cache:
    return cache[key]

# Bad comments - explain obvious WHAT
# Multiply amount by 0.08
tax = amount * 0.08

# Set x to 5
x = 5

# Docstrings for functions
def calculate_compound_interest(principal, rate, time, n=12):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial investment amount
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time (int): Number of years
        n (int): Number of times interest is compounded per year (default: 12)
    
    Returns:
        float: Final amount after compound interest
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    return principal * (1 + rate/n) ** (n*time)

# Class docstrings
class BankAccount:
    """
    Represent a bank account with basic operations.
    
    Attributes:
        account_number (str): Unique account identifier
        balance (float): Current account balance
        owner (str): Name of account owner
    
    Example:
        >>> account = BankAccount("123456", "John Doe")
        >>> account.deposit(1000)
        >>> account.get_balance()
        1000.0
    """
    
    def __init__(self, account_number, owner):
        """Initialize a new bank account."""
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.0
```

### Line Length and Spacing

**Definition:** Formatting guidelines for line length and whitespace.

**Explanation:** PEP 8 recommends keeping lines under 79 characters for code and 72 for docstrings. Proper spacing improves readability and makes code structure clear.

**Example:**
```python
# Keep lines under 79 characters
# Good - break long lines
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Good - use parentheses for line continuation
total = (first_value +
         second_value +
         third_value)

# Good - break long strings
message = ("This is a very long message that needs to be broken "
          "across multiple lines for better readability.")

# Spaces around operators
x = 5 + 3  # Good
x=5+3      # Bad

# One space after commas
my_list = [1, 2, 3, 4]  # Good
my_list = [1,2,3,4]     # Bad

# No space inside parentheses, brackets, or braces
my_function(arg1, arg2)  # Good
my_function( arg1, arg2 )  # Bad

my_list[0]  # Good
my_list[ 0 ]  # Bad

# Two blank lines between functions
def function_one():
    pass


def function_two():
    pass

# One blank line between methods in a class
class MyClass:
    def method_one(self):
        pass
    
    def method_two(self):
        pass

# Use blank lines to separate logical sections
def complex_function():
    # Setup
    data = load_data()
    
    # Process
    result = process_data(data)
    
    # Cleanup
    save_result(result)
    return result
```

---

## Quick Reference: Common Patterns

### File I/O Pattern

**Definition:** Standard approach to reading and writing files safely.

**Explanation:** Using `with` statements ensures files are properly closed even if errors occur. This pattern works for text, JSON, and binary files.

**Example:**
```python
# Reading text file
with open('file.txt', 'r') as f:
    contents = f.read()

# Reading line by line
with open('file.txt', 'r') as f:
    for line in f:
        process(line.rstrip())

# Writing to file
with open('file.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# Appending to file
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Reading and writing JSON
import json

# Write JSON
data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Binary files (images, etc.)
with open('image.jpg', 'rb') as f:
    image_data = f.read()

with open('copy.jpg', 'wb') as f:
    f.write(image_data)

# Check if file exists before reading
import os
if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        contents = f.read()
else:
    print("File not found")
```

### Error Handling Pattern

**Definition:** Comprehensive approach to handling errors in Python.

**Explanation:** Use try-except-else-finally blocks to handle errors gracefully. The else block runs if no errors occur, finally always runs for cleanup.

**Example:**
```python
# Basic error handling
try:
    result = risky_operation()
except SpecificError:
    handle_error()

# Multiple exception types
try:
    result = risky_operation()
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")
except Exception as e:
    print(f"Unexpected error: {e}")

# Complete pattern with else and finally
try:
    # Code that might fail
    file = open('data.txt', 'r')
    data = file.read()
    result = process_data(data)
except FileNotFoundError:
    print("File not found")
    result = None
except ValueError as e:
    print(f"Invalid data: {e}")
    result = None
except Exception as e:
    print(f"Unexpected error: {e}")
    result = None
else:
    # Runs only if no exception occurred
    print("Processing successful")
    save_result(result)
finally:
    # Always runs, even if there was an error
    if 'file' in locals():
        file.close()
    print("Cleanup complete")

# Context manager handles cleanup automatically
try:
    with open('data.txt', 'r') as f:
        data = f.read()
    result = process_data(data)
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
    result = None
else:
    print("Success!")
finally:
    print("Done")

# Raising exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Custom exceptions
class InvalidPasswordError(Exception):
    """Raised when password doesn't meet requirements."""
    pass

def set_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters")
```

### Class Definition Pattern

**Definition:** Standard structure for defining classes in Python.

**Explanation:** A well-structured class includes docstrings, initialization, properties, methods, and special methods. Follow this pattern for consistency.

**Example:**
```python
class MyClass:
    """
    Brief description of the class.
    
    Detailed explanation of what the class does and how to use it.
    
    Attributes:
        attribute_one: Description of attribute
        attribute_two: Description of attribute
    """
    
    # Class variables (shared by all instances)
    class_variable = "shared value"
    
    def __init__(self, param1, param2):
        """
        Initialize the class.
        
        Args:
            param1: Description of parameter
            param2: Description of parameter
        """
        # Instance variables (unique to each instance)
        self.attribute_one = param1
        self.attribute_two = param2
        self._private_attribute = None
    
    def public_method(self):
        """Public method that can be called from outside."""
        return self.attribute_one
    
    def _private_method(self):
        """Private method (by convention) for internal use."""
        return self._private_attribute
    
    @property
    def computed_property(self):
        """Property that computes a value."""
        return self.attribute_one + self.attribute_two
    
    @staticmethod
    def static_method(arg):
        """Method that doesn't need instance or class."""
        return arg * 2
    
    @classmethod
    def class_method(cls, arg):
        """Method that receives the class as first argument."""
        return cls(arg, arg)
    
    def __str__(self):
        """String representation for print()."""
        return f"MyClass({self.attribute_one}, {self.attribute_two})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"MyClass(param1={self.attribute_one!r}, param2={self.attribute_two!r})"
    
    def __eq__(self, other):
        """Check equality with another instance."""
        if not isinstance(other, MyClass):
            return False
        return (self.attribute_one == other.attribute_one and
                self.attribute_two == other.attribute_two)

# Using the class
obj = MyClass("value1", "value2")
print(obj.public_method())
print(obj.computed_property)
print(MyClass.static_method(5))
new_obj = MyClass.class_method("test")
```

### Main Guard Pattern

**Definition:** Standard pattern for making Python scripts both importable and executable.

**Explanation:** The main guard allows a file to be imported as a module or run as a script. Code under the guard only runs when the file is executed directly.

**Example:**
```python
def main():
    """Main program logic."""
    print("Running main program")
    result = do_something()
    print(f"Result: {result}")

def do_something():
    """Function that does something."""
    return "Done!"

def helper_function():
    """Helper function."""
    pass

# This only runs when the file is executed directly,
# not when it's imported as a module
if __name__ == '__main__':
    main()

# Alternative with argument parsing
import sys

def main(args):
    """Main program that accepts command line arguments."""
    if len(args) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)
    
    argument = args[1]
    print(f"Processing: {argument}")

if __name__ == '__main__':
    main(sys.argv)

# With argparse (better for complex arguments)
import argparse

def main():
    """Main program with argument parsing."""
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Processing {args.input}")
    
    # Process the file
    process_file(args.input, args.output)

if __name__ == '__main__':
    main()
```

### List Comprehension Pattern

**Definition:** Concise syntax for creating lists from iterables.

**Explanation:** List comprehensions are more readable and often faster than traditional loops. They can include filtering conditions and nested iterations.

**Example:**
```python
# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform items
names = ['alice', 'bob', 'charlie']
capitalized = [name.title() for name in names]
# Result: ['Alice', 'Bob', 'Charlie']

# Extract specific attributes
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
names = [user['name'] for user in users]
# Result: ['Alice', 'Bob', 'Charlie']

# With if-else: [expression_if_true if condition else expression_if_false for item in iterable]
labels = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
# Result: ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# Result: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ['hello', 'world', 'python', 'code']}
# Result: {4, 5, 6}

# Generator expression (memory efficient)
large_squares = (x**2 for x in range(1000000))
# Returns generator, not list - items created on demand
```

---

## Conclusion

This comprehensive Python reference guide covers the essential concepts from the Python Crash Course. Use it as a quick reference for:

- **Variables and Data Types**: Storing and manipulating data
- **Control Flow**: Making decisions and creating loops
- **Data Structures**: Lists, tuples, dictionaries for organizing data
- **Functions**: Creating reusable code blocks
- **Classes**: Object-oriented programming fundamentals
- **File I/O**: Reading and writing files safely
- **Error Handling**: Managing exceptions gracefully
- **Testing**: Ensuring code quality with unittest
- **Visualization**: Creating charts and graphs with Matplotlib and Plotly
- **Game Development**: Building games with Pygame

Remember:
1. **Practice regularly** - Programming is a skill that improves with practice
2. **Read other people's code** - Learn from well-written examples
3. **Write clean code** - Follow PEP 8 and best practices
4. **Comment thoughtfully** - Explain why, not what
5. **Test your code** - Write tests to catch bugs early
6. **Refactor often** - Improve code structure as you learn

Happy coding! 🐍
