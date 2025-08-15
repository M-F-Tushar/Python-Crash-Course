# Complete Guide to Python if Statements

## Table of Contents
1. [Introduction to if Statements](#introduction-to-if-statements)
2. [Conditional Tests](#conditional-tests)
3. [Types of if Statements](#types-of-if-statements)
4. [Using if Statements with Lists](#using-if-statements-with-lists)
5. [Styling Guidelines](#styling-guidelines)
6. [Practice Exercises](#practice-exercises)

---

## Introduction to if Statements

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's **if statement** allows you to examine the current state of a program and respond appropriately to that state.

### Simple Example: Car Names
```python
# cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

**Output:**
```
Audi
BMW
Subaru
Toyota
```

**Explanation:**
- The loop checks each car name
- If the car is 'bmw', it prints in uppercase
- Otherwise, it prints in title case
- This demonstrates how if statements can handle special cases differently

---

## Conditional Tests

At the heart of every if statement is an expression that can be evaluated as **True** or **False**, called a **conditional test**.

### 1. Checking for Equality

#### Basic Equality Test
```python
>>> car = 'bmw'
>>> car == 'bmw'
True
```

**Key Points:**
- Single equal sign (`=`) assigns a value
- Double equal sign (`==`) compares values
- Returns `True` if values match, `False` if they don't

#### When Values Don't Match
```python
>>> car = 'audi'
>>> car == 'bmw'
False
```

### 2. Case Sensitivity in Equality Tests

#### Case-Sensitive Comparison
```python
>>> car = 'Audi'
>>> car == 'audi'
False
```

#### Case-Insensitive Comparison
```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car  # Original value unchanged
'Audi'
```

**Important Note:** The `lower()` method doesn't change the original variable's value.

**Real-World Application:** Websites use this technique to ensure unique usernames regardless of capitalization.

### 3. Checking for Inequality

Use the **not equal** operator (`!=`) to test if two values are different.

```python
# toppings.py
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

**Output:** `Hold the anchovies!`

### 4. Numerical Comparisons

#### Equality with Numbers
```python
>>> age = 18
>>> age == 18
True
```

#### Inequality with Numbers
```python
# magic_number.py
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
```

#### Mathematical Comparisons
```python
>>> age = 19
>>> age < 21     # Less than
True
>>> age <= 21    # Less than or equal to
True
>>> age > 21     # Greater than
False
>>> age >= 21    # Greater than or equal to
False
```

### 5. Checking Multiple Conditions

#### Using `and` Keyword
Both conditions must be True for the overall expression to be True.

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False

>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

**Optional Parentheses for Clarity:**
```python
(age_0 >= 21) and (age_1 >= 21)
```

#### Using `or` Keyword
Only one condition needs to be True for the overall expression to be True.

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True

>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 6. Checking if a Value is in a List

#### Using `in` Keyword
```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 7. Checking if a Value is NOT in a List

#### Using `not in` Keywords
```python
# banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

**Output:** `Marie, you can post a response if you wish.`

### 8. Boolean Expressions

A **Boolean expression** is another name for a conditional test. Boolean values are either `True` or `False`.

```python
game_active = True
can_edit = False
```

Boolean values efficiently track program states or important conditions.

---

## Types of if Statements

### 1. Simple if Statements

**Syntax:**
```python
if conditional_test:
    do something
```

#### Single Action Example
```python
# voting.py
age = 19

if age >= 18:
    print("You are old enough to vote!")
```

#### Multiple Actions Example
```python
age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

**Output:**
```
You are old enough to vote!
Have you registered to vote yet?
```

### 2. if-else Statements

Execute one action when the test passes, another when it fails.

```python
age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

**Output:**
```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

### 3. if-elif-else Chain

Test multiple conditions, executing only the first one that passes.

#### Amusement Park Pricing Example
```python
# amusement_park.py
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

**Output:** `Your admission cost is $25.`

#### More Efficient Version
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

### 4. Using Multiple elif Blocks

#### Senior Discount Example
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20  # Senior discount

print(f"Your admission cost is ${price}.")
```

### 5. Omitting the else Block

Sometimes it's clearer to use a final `elif` instead of `else`:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

**Advantage:** Every block must pass a specific test, providing extra confidence in your code.

### 6. Testing Multiple Conditions

Use multiple simple `if` statements when you need to check all conditions (not just the first one that passes).

#### Pizza Toppings Example
```python
# toppings.py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

**Output:**
```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

#### What NOT to Do (Wrong Approach)
```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

**Wrong Output:**
```
Adding mushrooms.

Finished making your pizza!
```

**Rule:** Use `if-elif-else` when you want only one block to run. Use multiple `if` statements when multiple blocks need to run.

---

## Practice Exercises (5-1 to 5-7)

### Exercise 5-1: Conditional Tests
Write a series of conditional tests with predictions:

```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Create at least 10 tests total (5 True, 5 False)
```

### Exercise 5-2: More Conditional Tests
Test various comparison types:
- String equality and inequality
- Using `lower()` method
- Numerical comparisons
- `and` and `or` keywords
- Items in lists
- Items not in lists

### Exercise 5-3: Alien Colors #1
```python
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# Version that fails (no output)
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
```

### Exercise 5-4: Alien Colors #2
```python
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")
```

### Exercise 5-5: Alien Colors #3
```python
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")
```

### Exercise 5-6: Stages of Life
```python
age = 25

if age < 2:
    print("You're a baby.")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're an elder.")
```

### Exercise 5-7: Favorite Fruit
```python
favorite_fruits = ['banana', 'apple', 'mango']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
# Continue with more fruits...
```

---

## Using if Statements with Lists

### 1. Checking for Special Items

#### Pizza Topping Availability
```python
# toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

**Output:**
```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### 2. Checking That a List Is Not Empty

When a list might be empty, check before processing:

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

**Output:** `Are you sure you want a plain pizza?`

**Key Insight:** An empty list evaluates to `False` in an if statement.

### 3. Using Multiple Lists

Compare user requests against available options:

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

**Output:**
```
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

---

## Practice Exercises (5-8 to 5-11)

### Exercise 5-8: Hello Admin
```python
usernames = ['alice', 'bob', 'admin', 'charlie', 'dave']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
```

### Exercise 5-9: No Users
```python
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
```

### Exercise 5-10: Checking Usernames
```python
current_users = ['alice', 'bob', 'charlie', 'dave', 'eve']
new_users = ['frank', 'ALICE', 'grace', 'BOB', 'henry']

# Create lowercase version for comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, you need to enter a new username.")
    else:
        print(f"Great! {new_user} is available.")
```

### Exercise 5-11: Ordinal Numbers
```python
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
```

---

## Styling Guidelines

### PEP 8 Recommendations

#### Proper Spacing Around Operators
**Good:**
```python
if age < 4:
```

**Poor:**
```python
if age<4:
```

#### General Style Tips
- Use single spaces around comparison operators (`==`, `>=`, `<=`, etc.)
- Maintain consistent indentation (4 spaces recommended)
- Keep conditional tests readable and clear
- Use meaningful variable names

### Exercise 5-12: Styling Review
Review all programs written in this chapter and ensure proper styling of conditional tests.

### Exercise 5-13: Your Ideas
Record new programming ideas you'd like to explore:
- Games you might want to write
- Data sets to explore
- Web applications to create

---

## Summary

### Key Concepts Learned

1. **Conditional Tests:** Expressions that evaluate to `True` or `False`
2. **Simple if Statements:** Execute code when a condition is met
3. **if-else Chains:** Choose between two actions
4. **if-elif-else Chains:** Test multiple conditions, execute first match
5. **Multiple if Statements:** Test all conditions independently
6. **List Integration:** Use if statements to handle special items in lists
7. **Boolean Expressions:** Track program states efficiently

### Important Distinctions

- **if-elif-else:** Use when you want only one block to execute
- **Multiple if:** Use when multiple blocks might need to execute
- **Empty Lists:** Evaluate to `False` in conditional tests
- **Case Sensitivity:** Important in string comparisons; use `lower()` when needed

### Best Practices

- Check for empty lists before processing
- Use meaningful variable names
- Follow PEP 8 styling guidelines
- Test edge cases and special conditions
- Validate user input against available options

This foundation in conditional logic prepares you for more complex programming scenarios and sets the stage for learning about Python dictionaries in the next chapter.
