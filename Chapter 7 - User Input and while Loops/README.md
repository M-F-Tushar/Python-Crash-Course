# Python User Input and while Loops - Complete Guide

## Chapter Overview

This chapter covers two fundamental concepts in Python programming:
1. **User Input**: How to accept and work with user-provided data
2. **while Loops**: How to create programs that run continuously based on conditions

These concepts enable you to create fully interactive programs that respond to user needs and continue running as long as necessary.

---

## Part 1: User Input with the input() Function

### 1.1 How the input() Function Works

The `input()` function is Python's way of getting information from users. It:
- Pauses program execution
- Displays a prompt to the user
- Waits for user to type something and press Enter
- Returns what the user typed as a string
- Assigns that string to a variable for later use

#### Basic Example: Parrot Program
```python
# parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

**Output:**
```
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

**Key Points:**
- The text inside `input()` is the **prompt** - instructions for the user
- Whatever the user types becomes the value of the `message` variable
- The program waits indefinitely until the user presses Enter

### 1.2 Writing Clear Prompts

Good prompts are essential for user-friendly programs. They should:
- Clearly explain what information is needed
- Be easy to understand
- Include proper spacing for readability

#### Simple Prompt Example
```python
# greeter.py
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

**Output:**
```
Please enter your name: Eric
Hello, Eric!
```

**Best Practices:**
- Add a space after the colon for visual separation
- Use clear, specific language
- Tell users exactly what to enter

#### Multi-line Prompt Example
For longer prompts, build them using string concatenation:

```python
# greeter.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

**Output:**
```
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric
Hello, Eric!
```

**Explanation:**
- First line assigns initial text to `prompt` variable
- `+=` operator adds new text to the end of existing text
- `\n` creates a line break for better formatting
- Final prompt spans multiple lines but uses clean `input()` call

### 1.3 Working with Numerical Input

#### The String Problem
By default, `input()` always returns a **string**, even when users enter numbers:

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'  # Notice the quotes - this is a string!
```

#### Why This Causes Problems
```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18  # This will cause an error!
TypeError: unorderable types: str() >= int()
```

**Error Explanation:**
- Python can't compare a string ('21') to an integer (18)
- Strings and numbers are different data types
- Need to convert string to number first

#### Solution: Using int() Function

The `int()` function converts string representations of numbers to actual integers:

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)  # Convert string to integer
>>> age >= 18
True
```

#### Practical Example: Roller Coaster Height Check
```python
# rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

**Output:**
```
How tall are you, in inches? 71
You're tall enough to ride!
```

**Process Breakdown:**
1. User enters height as string (e.g., "71")
2. `int()` converts string to integer (71)
3. Now we can compare integer to integer (71 >= 48)
4. Comparison works correctly

### 1.4 The Modulo Operator (%)

The modulo operator divides one number by another and returns the **remainder**.

#### Basic Examples
```python
>>> 4 % 3  # 4 divided by 3 = 1 remainder 1
1
>>> 5 % 3  # 5 divided by 3 = 1 remainder 2
2
>>> 6 % 3  # 6 divided by 3 = 2 remainder 0
0
>>> 7 % 3  # 7 divided by 3 = 2 remainder 1
1
```

#### Practical Application: Even/Odd Detection
```python
# even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

**Logic Explanation:**
- Even numbers are divisible by 2 with no remainder
- If `number % 2 == 0`, the number is even
- If there's any remainder, the number is odd

**Output:**
```
Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
```

### 1.5 Try It Yourself Exercises (Part 1)

#### Exercise 7-1: Rental Car
**Task:** Write a program that asks what kind of rental car they want, then print a response.

**Solution:**
```python
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")
```

#### Exercise 7-2: Restaurant Seating
**Task:** Ask for dinner group size. If more than 8, they wait. Otherwise, table is ready.

**Solution:**
```python
group_size = input("How many people are in your dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")
```

#### Exercise 7-3: Multiples of Ten
**Task:** Ask for a number and report if it's a multiple of 10.

**Solution:**
```python
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
```

---

## Part 2: while Loops

### 2.1 Introduction to while Loops

**Comparison with for Loops:**
- **for loop**: Executes once for each item in a collection (fixed number of iterations)
- **while loop**: Continues running as long as a condition remains True (variable number of iterations)

### 2.2 Basic while Loop Structure

#### Simple Counting Example
```python
# counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

**Step-by-Step Execution:**
1. `current_number = 1` (initialize)
2. Check: `1 <= 5`? Yes, so enter loop
3. Print `1`
4. `current_number += 1` makes it `2`
5. Check: `2 <= 5`? Yes, continue...
6. This continues until `current_number` becomes `6`
7. Check: `6 <= 5`? No, exit loop

**Output:**
```
1
2
3
4
5
```

### 2.3 Interactive Programs with while Loops

#### Letting Users Control Program Flow
```python
# parrot.py - Version with user control
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```

**Key Components:**
- **Initialization**: `message = ""` gives Python something to check initially
- **Condition**: `message != 'quit'` keeps loop running until user types 'quit'
- **User Control**: User decides when to end program

**Problem with Above Code:**
The program prints 'quit' as if it were a regular message.

#### Improved Version with Conditional Check
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
```

**Output:**
```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### 2.4 Using Flags for Program Control

**What is a Flag?**
A flag is a variable that acts as a signal to determine whether a program should continue running. It's particularly useful when multiple conditions might end the program.

#### Flag-Based Program Structure
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True  # Flag variable
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False  # Change flag to stop loop
    else:
        print(message)
```

**Advantages of Using Flags:**
- Cleaner `while` statement (only checks one condition)
- Easy to add more exit conditions
- Better for complex programs (like games)
- More readable and maintainable code

**Example Use Cases:**
- Games (player loses, time runs out, cities destroyed)
- Data processing (error occurs, file ends, user stops)
- Menu systems (user selects exit, error occurs)

### 2.5 Using break to Exit Loops

The `break` statement immediately exits a loop, regardless of the loop condition.

#### Cities Program Example
```python
# cities.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:  # Infinite loop
    city = input(prompt)
    
    if city == 'quit':
        break  # Exit loop immediately
    else:
        print(f"I'd love to go to {city.title()}!")
```

**How it Works:**
1. `while True` creates an infinite loop
2. Loop continues forever unless `break` is reached
3. When user enters 'quit', `break` immediately exits loop
4. No need for flag variables or complex conditions

**Output:**
```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

### 2.6 Using continue to Skip Iterations

The `continue` statement skips the rest of the current loop iteration and returns to the loop's beginning.

#### Odd Numbers Example
```python
# counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Skip even numbers
    
    print(current_number)
```

**Execution Flow:**
1. `current_number` starts at 0
2. Increment to 1: `1 % 2 != 0`, so print 1
3. Increment to 2: `2 % 2 == 0`, so `continue` (skip printing)
4. Increment to 3: `3 % 2 != 0`, so print 3
5. Continue this pattern...

**Output:**
```
1
3
5
7
9
```

### 2.7 Avoiding Infinite Loops

**What is an Infinite Loop?**
A loop that never ends because its condition never becomes False.

#### Example of Infinite Loop (DON'T RUN THIS!)
```python
# This loop runs forever!
x = 1
while x <= 5:
    print(x)
    # Missing: x += 1
```

**Why it's Infinite:**
- `x` starts as 1
- Condition `x <= 5` is always True because `x` never changes
- Loop prints 1 forever

#### How to Stop Infinite Loops
- **In terminal**: Press `Ctrl+C`
- **In some editors**: Close the terminal window
- **Prevention**: Always ensure loop variables change in a way that will eventually make the condition False

#### Prevention Strategies
1. **Always modify the loop variable**
2. **Test your loops** with known inputs
3. **Use a counter** for safety in complex loops
4. **Double-check exit conditions**

### 2.8 Try It Yourself Exercises (Part 2)

#### Exercise 7-4: Pizza Toppings
**Task:** Loop asking for pizza toppings until user enters 'quit'.

**Solution:**
```python
prompt = "Enter a pizza topping (or 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
```

#### Exercise 7-5: Movie Tickets
**Task:** Loop asking for ages and showing ticket prices. Under 3: free, 3-12: $10, over 12: $15.

**Solution:**
```python
prompt = "Enter your age (or 'quit' to finish): "

while True:
    age_input = input(prompt)
    if age_input == 'quit':
        break
    
    age = int(age_input)
    
    if age < 3:
        price = 0
        print("Your ticket is free!")
    elif age <= 12:
        price = 10
        print(f"Your ticket costs ${price}.")
    else:
        price = 15
        print(f"Your ticket costs ${price}.")
```

#### Exercise 7-6: Three Exits
**Version 1 - Conditional test in while statement:**
```python
prompt = "Enter a pizza topping: "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
```

**Version 2 - Active variable:**
```python
prompt = "Enter a pizza topping: "
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
```

**Version 3 - Break statement:**
```python
prompt = "Enter a pizza topping: "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
```

#### Exercise 7-7: Infinity Loop
```python
# WARNING: This will run forever until you press Ctrl+C
x = 1
while x <= 5:
    print(x)
    # Intentionally omitting x += 1 to create infinite loop
```

---

## Part 3: Using while Loops with Lists and Dictionaries

### 3.1 Why Use while Loops with Data Structures?

**Key Principle:** Don't modify a list while iterating through it with a `for` loop, as this can cause Python to lose track of items.

**Solution:** Use `while` loops when you need to modify lists during iteration.

### 3.2 Moving Items Between Lists

#### User Verification System Example
```python
# confirmed_users.py
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

**Step-by-Step Process:**
1. **Initial State:**
   - `unconfirmed_users = ['alice', 'brian', 'candace']`
   - `confirmed_users = []`

2. **First Iteration:**
   - `pop()` removes 'candace' (last item)
   - Print "Verifying user: Candace"
   - Add 'candace' to `confirmed_users`

3. **Second Iteration:**
   - `pop()` removes 'brian'
   - Process and move 'brian'

4. **Third Iteration:**
   - `pop()` removes 'alice'
   - Process and move 'alice'

5. **Loop Ends:**
   - `unconfirmed_users` is now empty (evaluates to `False`)
   - All users are in `confirmed_users`

**Output:**
```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### 3.3 Removing All Instances of a Value

#### Problem with remove()
The `remove()` method only removes the **first** occurrence of a value:

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
pets.remove('cat')  # Only removes first 'cat'
print(pets)  # ['dog', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
```

#### Solution: while Loop with remove()
```python
# pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

**How It Works:**
1. Check if 'cat' is in the list
2. If yes, remove first occurrence of 'cat'
3. Repeat until 'cat' is no longer in list
4. Each iteration removes one 'cat'

**Output:**
```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

### 3.4 Filling Dictionaries with User Input

#### Polling Program Example
```python
# mountain_poll.py
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary.
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

**Program Flow:**
1. **Initialize:** Empty dictionary and active flag
2. **Loop While Active:**
   - Get name and mountain preference
   - Store in dictionary as key-value pair
   - Ask if more people want to participate
   - If 'no', set flag to False
3. **Display Results:** Iterate through dictionary and show all responses

**Sample Output:**
```
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
Lynn would like to climb Devil's Thumb.
Eric would like to climb Denali.
```

### 3.5 Try It Yourself Exercises (Part 3)

#### Exercise 7-8: Deli
**Task:** Make sandwich orders, move them to finished list as they're made.

**Solution:**
```python
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
```

#### Exercise 7-9: No Pastrami
**Task:** Remove all pastrami orders before making sandwiches.

**Solution:**
```python
sandwich_orders = ['veggie', 'pastrami', 'grilled cheese', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

print("Sorry, we're out of pastrami today!")

# Remove all pastrami orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make remaining sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
```

#### Exercise 7-10: Dream Vacation
**Task:** Poll users about dream vacation destinations.

**Solution:**
```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = place
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Dream Vacation Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
```

---

## Chapter Summary

### Key Concepts Learned

#### User Input
- **`input()` function**: Gets text from users, always returns strings
- **`int()` function**: Converts string numbers to integers for calculations
- **Clear prompts**: Essential for user-friendly programs
- **Modulo operator (%)**: Finds remainders, useful for even/odd detection

#### while Loops
- **Basic structure**: Continues while condition is True
- **User control**: Let users decide when to quit programs
- **Flags**: Variables that control program flow
- **`break` statement**: Exit loops immediately
- **`continue` statement**: Skip rest of current iteration
- **Infinite loops**: How to avoid and stop them

#### Advanced Applications
- **List modification**: Use while loops when changing lists during iteration
- **Moving items**: Transfer elements between lists safely
- **Removing duplicates**: Remove all instances of specific values
- **Dictionary filling**: Collect user data in key-value pairs
- **Interactive programs**: Combine input and loops for full user control

### Best Practices
1. Always provide clear, specific prompts
2. Convert input to appropriate data types
3. Test loops to ensure they terminate
4. Use flags for complex exit conditions
5. Avoid modifying lists during for loop iterations
6. Handle user input validation appropriately

This foundation enables you to create sophisticated, interactive programs that respond to user needs and continue running as long as necessary.
