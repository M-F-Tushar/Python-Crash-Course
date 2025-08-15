# Python Functions - Complete Study Guide

## Table of Contents
1. [Introduction to Functions](#introduction)
2. [Defining Functions](#defining-functions)
3. [Passing Information to Functions](#passing-information)
4. [Passing Arguments](#passing-arguments)
5. [Return Values](#return-values)
6. [Passing Lists](#passing-lists)
7. [Arbitrary Arguments](#arbitrary-arguments)
8. [Storing Functions in Modules](#modules)
9. [Styling Functions](#styling)
10. [Try It Yourself Exercises](#exercises)

---

## 1. Introduction to Functions {#introduction}

### What are Functions?
Functions are **named blocks of code** designed to perform one specific job. They make programs:
- Easier to write
- Easier to read  
- Easier to test
- Easier to fix

### Why Use Functions?
- **Reusability**: Write code once, use multiple times
- **Organization**: Break complex tasks into smaller parts
- **Maintainability**: Changes in one place affect all uses
- **Readability**: Descriptive names explain what code does

---

## 2. Defining Functions {#defining-functions}

### Basic Function Structure

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()  # Function call
```

**Output:**
```
Hello!
```

### Components Explained:
1. **`def` keyword**: Tells Python you're defining a function
2. **Function name**: `greet_user()` - descriptive name
3. **Parentheses**: Hold information the function needs (empty if none)
4. **Colon**: Ends the function definition line
5. **Docstring**: Comment describing what function does (optional but recommended)
6. **Function body**: Indented code that runs when function is called
7. **Function call**: Execute the function by writing its name with parentheses

---

## 3. Passing Information to Functions {#passing-information}

### Function with Parameters

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')
```

**Output:**
```
Hello, Jesse!
Hello, Sarah!
```

### Arguments vs Parameters

**Key Distinction:**
- **Parameter**: Variable in function definition (`username`)
- **Argument**: Actual value passed to function (`'jesse'`, `'sarah'`)

```python
def greet_user(username):  # 'username' is a PARAMETER
    print(f"Hello, {username.title()}!")

greet_user('jesse')  # 'jesse' is an ARGUMENT
```

---

## 4. Passing Arguments {#passing-arguments}

### 4.1 Positional Arguments

Arguments must be in the **same order** as parameters in function definition.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

**Output:**
```
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.
```

#### Order Matters!
```python
describe_pet('harry', 'hamster')  # Wrong order!
```

**Output:**
```
I have a harry.
My harry's name is Hamster.
```

### 4.2 Keyword Arguments

**Name-value pairs** that eliminate order confusion.

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')  # Same result!
```

**Benefits:**
- Order doesn't matter
- Clarifies what each value represents
- Prevents mistakes

### 4.3 Default Values

Set default values for parameters to simplify function calls.

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')  # Uses default 'dog'
describe_pet('harry', 'hamster')  # Overrides default
```

**Output:**
```
I have a dog.
My dog's name is Willie.

I have a hamster.
My hamster's name is Harry.
```

**Important Rule:** Parameters with default values must come **after** parameters without defaults.

### 4.4 Equivalent Function Calls

Multiple ways to call the same function:

```python
def describe_pet(pet_name, animal_type='dog'):
    # Function body here
    pass

# All equivalent for a dog named Willie:
describe_pet('willie')
describe_pet(pet_name='willie')

# All equivalent for a hamster named Harry:
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

### 4.5 Avoiding Argument Errors

**Common Error:**
```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()  # Missing arguments!
```

**Error Message:**
```
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```

**Tips:**
- Python tells you exactly what's missing
- Use descriptive parameter names for clearer error messages
- Check argument count and order

---

## 5. Return Values {#return-values}

### 5.1 Returning Simple Values

Functions can **return** values instead of just printing them.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

**Output:**
```
Jimi Hendrix
```

### 5.2 Making Arguments Optional

Use default values to make arguments optional.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

**Output:**
```
Jimi Hendrix
John Lee Hooker
```

**Key Points:**
- Empty strings evaluate to `False` in conditionals
- Non-empty strings evaluate to `True`
- Optional parameters should come last

### 5.3 Returning Dictionaries

Functions can return complex data structures.

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

**Output:**
```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

**About `None`:**
- Special value representing "no value"
- Evaluates to `False` in conditionals
- Used as placeholder for optional values

### 5.4 Using Functions with while Loops

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

**Sample Run:**
```
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

---

## 6. Passing Lists {#passing-lists}

### 6.1 Passing Lists to Functions

Functions can work directly with lists.

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

**Output:**
```
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

### 6.2 Modifying Lists in Functions

Functions can **permanently modify** lists passed to them.

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

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

**Output:**
```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

**Benefits of Using Functions:**
- Code is organized and easier to understand
- Each function has one specific job
- Easy to extend and maintain
- Reusable code

### 6.3 Preventing Function from Modifying Lists

Use **slice notation** `[:]` to pass a copy of the list.

```python
# Pass original list (will be modified)
print_models(unprinted_designs, completed_models)

# Pass copy of list (original unchanged)
print_models(unprinted_designs[:], completed_models)
```

**When to Use Copies:**
- When you need to preserve the original list
- For record-keeping purposes
- When function shouldn't modify input data

**When to Use Originals:**
- More efficient (saves time and memory)
- When modification is intended
- With large lists (copying can be expensive)

---

## 7. Arbitrary Arguments {#arbitrary-arguments}

### 7.1 Arbitrary Number of Arguments (*args)

When you don't know how many arguments a function will receive.

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

**Output:**
```
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

**Better Implementation:**
```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

**Output:**
```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

**Key Points:**
- `*toppings` creates a tuple containing all arguments
- Works with any number of arguments
- Common parameter name: `*args`

### 7.2 Mixing Positional and Arbitrary Arguments

Required parameters must come **before** arbitrary arguments.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**Output:**
```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### 7.3 Arbitrary Keyword Arguments (**kwargs)

Accept arbitrary number of keyword arguments.

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
```

**Output:**
```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

**Key Points:**
- `**user_info` creates a dictionary of keyword arguments
- Can mix positional, keyword, and arbitrary arguments
- Common parameter name: `**kwargs`

---

## 8. Storing Functions in Modules {#modules}

### 8.1 Creating a Module

**pizza.py** (the module):
```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

### 8.2 Importing Entire Module

**making_pizzas.py**:
```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**Syntax:** `module_name.function_name()`

### 8.3 Importing Specific Functions

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**Multiple functions:**
```python
from module_name import function_0, function_1, function_2
```

### 8.4 Using Aliases for Functions

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**General syntax:**
```python
from module_name import function_name as fn
```

### 8.5 Using Aliases for Modules

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**General syntax:**
```python
import module_name as mn
```

### 8.6 Importing All Functions

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**⚠️ Warning:** Not recommended for larger modules - can cause naming conflicts.

---

## 9. Styling Functions {#styling}

### Function Naming Conventions
- Use **descriptive names**
- Use **lowercase letters and underscores**
- Same rules apply to module names

### Documentation
- Every function should have a **docstring**
- Appears immediately after function definition
- Uses triple quotes
- Explains what the function does concisely

### Parameter Formatting
```python
# Correct - no spaces around = for default values
def function_name(parameter_0, parameter_1='default value')

# Correct - no spaces around = for keyword arguments  
function_name(value_0, parameter_1='value')
```

### Line Length
- Limit lines to **79 characters** (PEP 8)
- For long parameter lists:

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```

### Function Separation
- Separate functions with **two blank lines**
- Makes code easier to read

### Import Statements
- Place all imports at the **beginning of file**
- Exception: comments describing the program

---

## 10. Try It Yourself Exercises {#exercises}

### Exercise 8-1: Message
**Task:** Write a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. Call the function.

**Solution:**
```python
def display_message():
    """Display a message about what I'm learning."""
    print("I'm learning about functions in Python!")

display_message()
```

### Exercise 8-2: Favorite Book  
**Task:** Write a function called `favorite_book()` that accepts one parameter, `title`. The function should print a message like "One of my favorite books is Alice in Wonderland." Call the function.

**Solution:**
```python
def favorite_book(title):
    """Display a message about a favorite book."""
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
favorite_book("To Kill a Mockingbird")
```

### Exercise 8-3: T-Shirt
**Task:** Write a function called `make_shirt()` that accepts a size and message text. Print a summary. Call using positional arguments, then keyword arguments.

**Solution:**
```python
def make_shirt(size, message):
    """Summarize a t-shirt order."""
    print(f"Making a {size} t-shirt with the message: '{message}'")

# Positional arguments
make_shirt('large', 'Python is awesome!')

# Keyword arguments  
make_shirt(message='Code every day!', size='medium')
```

### Exercise 8-4: Large Shirts
**Task:** Modify `make_shirt()` so shirts are large by default with message "I love Python". Make a large shirt and medium shirt with default message, and any size with different message.

**Solution:**
```python
def make_shirt(size='large', message='I love Python'):
    """Summarize a t-shirt order."""
    print(f"Making a {size} t-shirt with the message: '{message}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt('medium')

# Custom size and message
make_shirt('small', 'Python rocks!')
```

### Exercise 8-5: Cities
**Task:** Write `describe_city()` that accepts city name and country. Give country parameter a default value. Call for three cities, at least one not in default country.

**Solution:**
```python
def describe_city(city, country='USA'):
    """Describe a city and its country."""
    print(f"{city} is in {country}.")

describe_city('New York')
describe_city('Los Angeles')
describe_city('Paris', 'France')
```

### Exercise 8-6: City Names
**Task:** Write `city_country()` that takes city name and country, returns formatted string like "Santiago, Chile". Call with at least three city-country pairs.

**Solution:**
```python
def city_country(city, country):
    """Return a formatted city-country string."""
    return f"{city}, {country}"

print(city_country('Santiago', 'Chile'))
print(city_country('Tokyo', 'Japan'))  
print(city_country('Cairo', 'Egypt'))
```

### Exercise 8-7: Album
**Task:** Write `make_album()` that builds a dictionary with artist and album title. Add optional parameter for number of songs.

**Solution:**
```python
def make_album(artist, title, songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Three albums without song count
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'The Wall')
album3 = make_album('Led Zeppelin', 'IV')

print(album1)
print(album2)
print(album3)

# Album with song count
album4 = make_album('Queen', 'Bohemian Rhapsody', 12)
print(album4)
```

### Exercise 8-8: User Albums
**Task:** Start with Exercise 8-7. Write a while loop allowing users to enter artist and title. Call `make_album()` with user input. Include quit value.

**Solution:**
```python
def make_album(artist, title, songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nEnter album information (or 'quit' to stop):")
    
    artist = input("Artist name: ")
    if artist == 'quit':
        break
        
    title = input("Album title: ")
    if title == 'quit':
        break
    
    album = make_album(artist, title)
    print(album)
```

### Exercise 8-9: Messages
**Task:** Make a list of short text messages. Pass to function `show_messages()` which prints each message.

**Solution:**
```python
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

text_messages = [
    "Hello there!",
    "How are you doing?",
    "Python is fun!",
    "Keep coding!"
]

show_messages(text_messages)
```

### Exercise 8-10: Sending Messages  
**Task:** Start with Exercise 8-9. Write `send_messages()` that prints each message and moves it to new list `sent_messages`. Print both lists after calling function.

**Solution:**
```python
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Send each message and move to sent list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

text_messages = ["Hello!", "How are you?", "Python rocks!"]
sent_messages = []

print("Original messages:")
print(text_messages)

send_messages(text_messages, sent_messages)

print("\nAfter sending:")
print(f"Text messages: {text_messages}")
print(f"Sent messages: {sent_messages}")
```

### Exercise 8-11: Archived Messages
**Task:** Start with Exercise 8-10. Call `send_messages()` with a copy of the message list. Print both lists to show original retained its messages.

**Solution:**
```python
def send_messages(messages, sent_messages):
    """Send each message and move to sent list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

text_messages = ["Hello!", "How are you?", "Python rocks!"]
sent_messages = []

print("Original messages:")
print(text_messages)

# Send a copy of messages
send_messages(text_messages[:], sent_messages)

print("\nAfter sending:")
print(f"Original messages: {text_messages}")
print(f"Sent messages: {sent_messages}")
```

### Exercise 8-12: Sandwiches
**Task:** Write function that accepts list of sandwich items. Function should have one parameter collecting as many items as provided. Print sandwich summary. Call three times with different numbers of arguments.

**Solution:**
```python
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey')
make_sandwich('ham', 'cheese', 'lettuce')  
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')
```

### Exercise 8-13: User Profile
**Task:** Start with `user_profile.py`. Build profile of yourself using `build_profile()` with your first/last names and three other key-value pairs.

**Solution:**
```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('John', 'Doe',
                          location='New York',
                          field='Software Engineering',
                          hobby='Photography')

print(my_profile)
```

### Exercise 8-14: Cars
**Task:** Write function storing car info in dictionary. Always receive manufacturer and model. Accept arbitrary keyword arguments. Call with required info and two other name-value pairs.

**Solution:**
```python
def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car2 = make_car('toyota', 'camry', color='red', year=2023, hybrid=True)
print(car2)
```

### Exercise 8-15: Printing Models
**Task:** Put functions from `printing_models.py` in separate file `printing_functions.py`. Write import statement and modify main file to use imported functions.

**printing_functions.py:**
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
```

**printing_models.py:**
```python
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
```

### Exercise 8-16: Imports
**Task:** Using a program with one function, store function in separate file. Import function using each import approach.

**math_functions.py:**
```python
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b
```

**main.py:**
```python
# Method 1: import module_name
import math_functions
result = math_functions.add_numbers(5, 3)
print(f"Method 1: {result}")

# Method 2: from module_name import function_name  
from math_functions import add_numbers
result = add_numbers(5, 3)
print(f"Method 2: {result}")

# Method 3: from module_name import function_name as fn
from math_functions import add_numbers as add
result = add(5, 3)
print(f"Method 3: {result}")

# Method 4: import module_name as mn
import math_functions as mf
result = mf.add_numbers(5, 3)
print(f"Method 4: {result}")

# Method 5: from module_name import *
from math_functions import *
result = add_numbers(5, 3)  
print(f"Method 5: {result}")
```

### Exercise 8-17: Styling Functions
**Task:** Choose three programs from this chapter and ensure they follow styling guidelines.

**Key styling points to check:**
- Descriptive function names with lowercase and underscores
- Docstrings for all functions
- Proper spacing around default values and keyword arguments
- Lines under 79 characters
- Two blank lines between functions
- Import statements at top of file

---

## Summary

Functions are fundamental building blocks in Python programming that provide:

### Key Benefits:
- **Code Reusability**: Write once, use multiple times
- **Organization**: Break complex problems into smaller, manageable pieces  
- **Maintainability**: Changes in one place affect all uses
- **Readability**: Descriptive names make code self-documenting
- **Testing**: Easier to test individual components

### Core Concepts Mastered:
1. **Function Definition**: Using `def` keyword, parameters, docstrings
2. **Argument Types**: Positional, keyword, default values, arbitrary arguments
3. **Return Values**: Returning simple values, dictionaries, optional returns
4. **List Handling**: Passing, modifying, and protecting lists in functions
5. **Modules**: Organizing functions in separate files, various import methods
6. **Best Practices**: Styling, documentation, and code organization

### Next Steps:
Understanding functions prepares you for more advanced topics like classes, which combine functions and data into powerful, reusable objects. Functions form the foundation of good programming practices and will be used throughout your Python journey.

The skills learned in this chapter - breaking problems into functions, handling different types of arguments, and organizing code into modules - are essential for writing clean, professional Python code.
