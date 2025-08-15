# Complete Python Dictionaries Guide - Chapter 6

## Table of Contents
1. [Introduction to Dictionaries](#introduction)
2. [Working with Dictionaries](#working-with-dictionaries)
3. [Dictionary Operations](#dictionary-operations)
4. [Looping Through Dictionaries](#looping-through-dictionaries)
5. [Nesting](#nesting)
6. [Try It Yourself Exercises](#exercises)
7. [Summary](#summary)

---

## Introduction to Dictionaries {#introduction}

### What are Dictionaries?
Python dictionaries allow you to connect pieces of related information. They can store an almost limitless amount of information and enable you to model real-world objects accurately.

### Real-World Applications
- Store person information (name, age, location, profession)
- Match related data (words-meanings, names-favorite numbers, mountains-elevations)
- Model game objects with multiple properties

### Simple Dictionary Example
```python
# Basic alien dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # Output: green
print(alien_0['points']) # Output: 5
```

**Key Points:**
- Dictionaries store key-value pairs
- Values are accessed using keys
- Useful for modeling real-world situations

---

## Working with Dictionaries {#working-with-dictionaries}

### Dictionary Structure
- **Definition**: A collection of key-value pairs
- **Syntax**: Wrapped in braces `{}` with key-value pairs inside
- **Key-Value Pairs**: Connected by colons, separated by commas

```python
# Dictionary structure
alien_0 = {'color': 'green', 'points': 5}
```

### Key Components
1. **Keys**: Identifiers to access values
2. **Values**: Can be numbers, strings, lists, or other dictionaries
3. **Pairs**: Each key connects to exactly one value

---

## Dictionary Operations {#dictionary-operations}

### 1. Accessing Values

#### Basic Access
```python
alien_0 = {'color': 'green'}
print(alien_0['color'])  # Output: green
```

#### Practical Example
```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# Output: You just earned 5 points!
```

### 2. Adding New Key-Value Pairs

#### Adding Single Pairs
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # {'color': 'green', 'points': 5}

# Add position coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# Output: {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```

**Important Note**: As of Python 3.7, dictionaries retain insertion order.

### 3. Starting with Empty Dictionary

#### Building Dictionary Gradually
```python
alien_0 = {}  # Empty dictionary
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)  # Output: {'color': 'green', 'points': 5}
```

**Use Cases**:
- Storing user-supplied data
- Generating key-value pairs automatically
- Building dictionaries programmatically

### 4. Modifying Values

#### Simple Modification
```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")  # The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")  # The alien is now yellow.
```

#### Complex Modification Example
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Determine movement based on speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:  # fast alien
    x_increment = 3

# Update position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
# Output: Original position: 0
#         New position: 2
```

### 5. Removing Key-Value Pairs

#### Using del Statement
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)  # {'color': 'green'}
```

**Warning**: Deleted key-value pairs are removed permanently.

### 6. Dictionary of Similar Objects

#### Favorite Languages Poll Example
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Access specific person's choice
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# Output: Sarah's favorite language is C.
```

**Formatting Tips**:
- Break large dictionaries across multiple lines
- Indent key-value pairs consistently
- Include comma after last pair for easier additions

### 7. Using get() Method for Safe Access

#### Problem with Direct Access
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])  # KeyError: 'points'
```

#### Solution with get()
```python
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)  # Output: No point value assigned.
```

**get() Method Parameters**:
1. **First argument**: Key to search for
2. **Second argument** (optional): Default value if key doesn't exist
3. **No second argument**: Returns `None` if key doesn't exist

---

## Looping Through Dictionaries {#looping-through-dictionaries}

### 1. Looping Through All Key-Value Pairs

#### Basic Syntax
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

**Output:**
```
Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi
```

#### Practical Example with Descriptive Names
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
```

**Output:**
```
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

### 2. Looping Through Keys Only

#### Basic Key Iteration
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
```

**Output:**
```
Jen
Sarah
Edward
Phil
```

**Note**: `favorite_languages.keys()` is equivalent to just `favorite_languages`

#### Conditional Processing During Key Iteration
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```

**Output:**
```
Hi Jen.
Hi Sarah.
    Sarah, I see you love C!
Hi Edward.
Hi Phil.
    Phil, I see you love Python!
```

#### Checking for Specific Keys
```python
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# Output: Erin, please take our poll!
```

### 3. Looping Through Keys in Order

#### Sorting Keys
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

**Output:**
```
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### 4. Looping Through Values Only

#### Basic Value Iteration
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

**Output:**
```
The following languages have been mentioned:
Python
C
Python
Ruby
```

#### Removing Duplicates with set()
```python
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

**Output:**
```
The following languages have been mentioned:
Python
C
Ruby
```

**Set Properties**:
- Collections where each item must be unique
- Can be created with `{}` (no key-value pairs)
- Do not retain specific order
- Useful for eliminating duplicates

---

## Nesting {#nesting}

### 1. List of Dictionaries

#### Basic Example
```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

**Output:**
```
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

#### Generating Multiple Dictionaries
```python
# Create empty list for aliens
aliens = []

# Generate 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Display first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
```

**Output:**
```
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
Total number of aliens: 30
```

#### Modifying Dictionaries in List
```python
# Create 30 green aliens
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change first 3 aliens to yellow
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Display first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
```

**Output:**
```
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
```

### 2. List Inside Dictionary

#### Pizza Ordering Example
```python
# Store pizza information
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```

**Output:**
```
You ordered a thick-crust pizza with the following toppings:
    mushrooms
    extra cheese
```

#### Multiple Favorite Languages
```python
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

**Output:**
```
Jen's favorite languages are:
    Python
    Ruby

Sarah's favorite languages are:
    C

Phil's favorite languages are:
    Python
    Haskell

Edward's favorite languages are:
    Ruby
    Go
```

**Enhancement Idea**: Add conditional logic to handle singular vs plural language preferences.

### 3. Dictionary Inside Dictionary

#### User Information System
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

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

**Output:**
```
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

**Best Practice**: Keep nested dictionary structures identical for easier processing.

**Warning**: Avoid excessive nesting - if nesting goes too deep, consider simplifying the data structure.

---

## Try It Yourself Exercises {#exercises}

### Exercise 6-1: Person
**Task**: Use a dictionary to store information about a person you know. Store their first name, last name, age, and city. Print each piece of information.

**Solution Approach**:
```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
```

### Exercise 6-2: Favorite Numbers
**Task**: Use a dictionary to store people's favorite numbers. Print each person's name and their favorite number.

**Solution Approach**:
```python
favorite_numbers = {
    'alice': 7,
    'bob': 42,
    'charlie': 3,
    'diana': 13,
    'eve': 21
}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")
```

### Exercise 6-3: Glossary
**Task**: Create a programming glossary with 5 terms and their meanings.

**Solution Approach**:
```python
glossary = {
    'variable': 'A storage location with an associated name that contains data',
    'function': 'A reusable block of code that performs a specific task',
    'loop': 'A programming construct that repeats a block of code',
    'list': 'An ordered collection of items that can be modified',
    'dictionary': 'A collection of key-value pairs'
}

for term, definition in glossary.items():
    print(f"{term.title()}:")
    print(f"\t{definition}\n")
```

### Exercise 6-4: Glossary 2
**Task**: Use a loop instead of multiple print() calls for the glossary. Add 5 more terms.

**Solution Enhancement**: Use the loop structure from Exercise 6-3 with additional terms.

### Exercise 6-5: Rivers
**Task**: Create a dictionary with rivers and countries. Print sentences, river names, and country names separately.

**Solution Approach**:
```python
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print sentences
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print river names
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print countries
print("\nCountries:")
for country in rivers.values():
    print(country.title())
```

### Exercise 6-6: Polling
**Task**: Create a list of people who should take the poll. Check if they've already participated.

**Solution Approach**:
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_candidates = ['jen', 'sarah', 'alice', 'bob', 'edward']

for candidate in poll_candidates:
    if candidate in favorite_languages:
        print(f"{candidate.title()}, thank you for taking the poll!")
    else:
        print(f"{candidate.title()}, please take our poll!")
```

### Exercise 6-7: People
**Task**: Create a list of dictionaries representing different people.

**Solution Approach**:
```python
person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
person2 = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'Los Angeles'}
person3 = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Chicago'}

people = [person1, person2, person3]

for person in people:
    print(f"\nPerson Information:")
    for key, value in person.items():
        print(f"\t{key.replace('_', ' ').title()}: {value}")
```

### Exercise 6-8: Pets
**Task**: Create dictionaries representing different pets with animal type and owner information.

**Solution Approach**:
```python
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'fish', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nPet Information:")
    print(f"\tAnimal: {pet['animal'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")
```

### Exercise 6-9: Favorite Places
**Task**: Store multiple favorite places for each person.

**Solution Approach**:
```python
favorite_places = {
    'alice': ['paris', 'tokyo', 'new york'],
    'bob': ['london', 'sydney'],
    'charlie': ['rome', 'barcelona', 'amsterdam', 'berlin']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"\t{place.title()}")
```

### Exercise 6-10: Favorite Numbers (Enhanced)
**Task**: Modify Exercise 6-2 to allow multiple favorite numbers per person.

**Solution Approach**:
```python
favorite_numbers = {
    'alice': [7, 14, 21],
    'bob': [42],
    'charlie': [3, 9, 27],
    'diana': [13, 26],
    'eve': [21, 42, 63]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")
    for number in numbers:
        print(f"\t{number}")
```

### Exercise 6-11: Cities
**Task**: Create nested dictionaries with city information.

**Solution Approach**:
```python
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_000_000,
        'fact': 'largest metropolitan area in the world'
    },
    'paris': {
        'country': 'france',
        'population': 2_200_000,
        'fact': 'known as the city of light'
    },
    'sydney': {
        'country': 'australia',
        'population': 5_300_000,
        'fact': 'famous for its opera house'
    }
}

for city_name, city_info in cities.items():
    print(f"\n{city_name.title()}:")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']:,}")
    print(f"\tFact: {city_info['fact'].title()}")
```

### Exercise 6-12: Extensions
**Task**: Extend one of the example programs with new features.

**Ideas for Extension**:
- Add data validation
- Implement user input functionality
- Create more complex nested structures
- Add statistical analysis features
- Implement data export capabilities

---

## Summary {#summary}

### Key Concepts Learned

#### Dictionary Fundamentals
- **Definition**: Collections of key-value pairs
- **Structure**: Wrapped in braces `{}` with key-value pairs
- **Access**: Use keys in square brackets `dictionary[key]`
- **Dynamic**: Can be modified after creation

#### Essential Operations
1. **Creating**: Empty `{}` or with initial pairs
2. **Accessing**: Direct access or `.get()` method
3. **Adding**: `dictionary[new_key] = value`
4. **Modifying**: `dictionary[existing_key] = new_value`
5. **Removing**: `del dictionary[key]`

#### Looping Techniques
1. **Key-Value Pairs**: `for key, value in dict.items()`
2. **Keys Only**: `for key in dict.keys()` or `for key in dict`
3. **Values Only**: `for value in dict.values()`
4. **Ordered Keys**: `for key in sorted(dict.keys())`

#### Nesting Strategies
1. **List of Dictionaries**: Store multiple objects
2. **List in Dictionary**: Multiple values per key
3. **Dictionary in Dictionary**: Nested object properties

#### Best Practices
- Use descriptive variable names in loops
- Check for key existence with `.get()`
- Keep nested structures simple
- Use consistent dictionary structures
- Consider using sets to eliminate duplicates

### Practical Applications
- User management systems
- Game object modeling
- Data organization and retrieval
- Configuration storage
- Polling and survey data
- Inventory management

### Next Steps
The chapter prepares you for:
- While loops (Chapter 7)
- User input handling
- Interactive program development
- More complex data manipulation

This comprehensive understanding of dictionaries provides a solid foundation for building more sophisticated Python programs that can handle complex data relationships and user interactions.
