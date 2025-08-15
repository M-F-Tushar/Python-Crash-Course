# Python Files and Exceptions - Complete Guide

## Chapter Overview
This chapter covers essential skills for making Python programs more relevant and usable by:
- Working with files to analyze large amounts of data
- Handling errors gracefully to prevent program crashes
- Managing exceptions with try-except blocks
- Using the JSON module to save and load user data
- Making programs more robust and user-friendly

---

## Part 1: Reading from Files

### 1.1 Reading an Entire File

#### Concept
Files contain vast amounts of data (weather, traffic, socioeconomic, literary works). Reading files is crucial for data analysis and information processing.

#### Basic File Reading Structure
```python
with open('filename.txt') as file_object:
    contents = file_object.read()
print(contents)
```

#### Detailed Example: Reading Pi Digits
**File: pi_digits.txt**
```
3.1415926535
 8979323846
 2643383279
```

**Code: file_reader.py**
```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
```

#### Key Components Explained:

1. **`open()` Function**: 
   - Takes filename as argument
   - Returns file object representing the file
   - Python searches in the current directory

2. **`with` Statement**:
   - Automatically closes file when block finishes
   - Prevents data loss from improperly closed files
   - No need to manually call `close()`

3. **`read()` Method**:
   - Reads entire file content as one string
   - Returns empty string at end of file (appears as blank line)

#### Removing Extra Whitespace
```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # Removes trailing whitespace
```

### 1.2 File Paths

#### Understanding File Paths
When files aren't in the same directory as your program, you need to specify the path.

#### Relative File Paths
```python
# File structure: python_work/text_files/filename.txt
with open('text_files/filename.txt') as file_object:
    # Code here
```
- **Relative path**: Looks relative to current program location
- Use forward slashes (/) even on Windows

#### Absolute File Paths
```python
file_path = '/home/user/other_files/text_files/filename.txt'
with open(file_path) as file_object:
    # Code here
```
- **Absolute path**: Complete path from root directory
- Works regardless of program location
- Assign to variable for readability

#### Important Path Notes:
- Windows uses backslashes (\) but forward slashes (/) work in code
- Backslashes need escaping: `"C:\\path\\to\\file.txt"`
- Store files in same directory or subdirectory for simplicity

### 1.3 Reading Line by Line

#### When to Use Line-by-Line Reading
- Searching for specific information
- Processing large files efficiently
- Modifying text line by line
- Working with structured data

#### Basic Line-by-Line Example
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
```

#### Problem: Extra Blank Lines
Each line has invisible newline character + print() adds another newline = double spacing

#### Solution: Using rstrip()
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # Removes trailing whitespace from each line
```

### 1.4 Making a List of Lines from a File

#### Purpose
Store file contents in a list to work with data outside the `with` block.

#### Using readlines() Method
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # Returns list of lines

for line in lines:
    print(line.rstrip())
```

#### Key Points:
- `readlines()` creates list where each item is a line from file
- List persists after `with` block ends
- Each list item corresponds to file line
- Useful for processing data after file is closed

### 1.5 Working with File Contents

#### Building a String from Multiple Lines
**Goal**: Create single string containing all pi digits without whitespace

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()  # Remove newlines

print(pi_string)
print(len(pi_string))
```

**Output:**
```
3.1415926535 8979323846 2643383279
36
```

#### Removing All Whitespace
```python
for line in lines:
    pi_string += line.strip()  # Remove all leading/trailing whitespace

print(pi_string)
print(len(pi_string))
```

**Output:**
```
3.141592653589793238462643383279
32
```

### 1.6 Large Files: One Million Digits

#### Handling Large Files
Python has no inherent limit - can work with as much data as system memory allows.

```python
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")  # Show first 52 characters
print(len(pi_string))
```

**Output:**
```
3.14159265358979323846264338327950288419716939937510...
1000002
```

### 1.7 Practical Example: Birthday in Pi

#### Finding Patterns in Large Data
```python
# After building pi_string from million digits
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

**Example Run:**
```
Enter your birthdate, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!
```

### 1.8 Try It Yourself Exercises

#### Exercise 10-1: Learning Python
Write a program that:
1. Creates a file with lines starting "In Python you can..."
2. Reads and prints contents three ways:
   - Reading entire file
   - Looping over file object
   - Storing lines in list and working outside `with` block

**Solution Approach:**
```python
# Create file
filename = 'learning_python.txt'
with open(filename, 'w') as file_object:
    file_object.write("In Python you can create variables.\n")
    file_object.write("In Python you can use loops.\n")
    file_object.write("In Python you can work with files.\n")

# Method 1: Read entire file
print("Reading entire file:")
with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Method 2: Loop over file object
print("\nLooping over file object:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Method 3: Store in list
print("\nWorking with list outside with block:")
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
```

#### Exercise 10-2: Learning C
Use `replace()` method to substitute "Python" with "C" in each line.

**Solution:**
```python
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line.rstrip())
```

---

## Part 2: Writing to Files

### 2.1 Writing to an Empty File

#### Basic File Writing Structure
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

#### File Opening Modes
- `'r'`: Read mode (default)
- `'w'`: Write mode (overwrites existing file)
- `'a'`: Append mode (adds to end of file)
- `'r+'`: Read and write mode

#### Important Warnings:
- **Write mode ('w') overwrites existing files completely**
- **Python creates file if it doesn't exist**
- **Only strings can be written to text files** (use `str()` for numbers)

### 2.2 Writing Multiple Lines

#### Problem: Lines Run Together
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```

**Result:** `I love programming.I love creating new games.`

#### Solution: Add Newline Characters
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

**Result:**
```
I love programming.
I love creating new games.
```

### 2.3 Appending to a File

#### Purpose of Append Mode
Add content without erasing existing content.

```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

**Final File Content:**
```
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
```

### 2.4 Try It Yourself Exercises (Writing)

#### Exercise 10-3: Guest
Write a program that prompts for user's name and writes it to `guest.txt`.

**Solution:**
```python
name = input("What's your name? ")
with open('guest.txt', 'w') as file_object:
    file_object.write(name)
```

#### Exercise 10-4: Guest Book
Create a loop that prompts for names and records visits.

**Solution:**
```python
filename = 'guest_book.txt'
print("Enter 'quit' to stop.")

while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    
    print(f"Hello, {name}!")
    with open(filename, 'a') as file_object:
        file_object.write(f"{name} visited.\n")
```

#### Exercise 10-5: Programming Poll
Ask why people like programming and store responses.

**Solution:**
```python
filename = 'programming_poll.txt'
print("Enter 'quit' to stop.")

while True:
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")
```

---

## Part 3: Exceptions

### 3.1 Understanding Exceptions

#### What Are Exceptions?
- Special objects Python creates when errors occur
- Allow programs to continue running instead of crashing
- Provide user-friendly error messages instead of tracebacks

#### Exception Handling Benefits:
- Prevent program crashes
- Provide meaningful error messages
- Continue execution when possible
- Handle external dependencies gracefully

### 3.2 Handling ZeroDivisionError

#### The Problem
```python
print(5/0)
```

**Result:**
```
Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
ZeroDivisionError: division by zero
```

#### The Solution: try-except Blocks
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Result:** `You can't divide by zero!`

#### How try-except Works:
1. Python attempts code in `try` block
2. If error occurs, Python looks for matching `except` block
3. If match found, runs code in `except` block
4. Program continues after try-except block

### 3.3 Using Exceptions to Prevent Crashes

#### Real-World Example: Division Calculator
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

#### Problem: Crashes on Invalid Input
- Division by zero causes crash
- Non-numeric input causes ValueError
- Users see confusing tracebacks

#### Solution: Add Exception Handling
```python
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

### 3.4 The else Block

#### Purpose of else Block
- Contains code that should run only if `try` block succeeds
- Separates error-prone code from code that depends on success
- Makes code structure clearer

#### Structure:
```python
try:
    # Code that might cause error
    risky_operation()
except SpecificError:
    # Handle specific error
    print("Error occurred!")
else:
    # Code that runs only if try succeeds
    print("Success!")
```

### 3.5 Handling FileNotFoundError

#### Common File-Related Problems:
- File doesn't exist
- File in different location
- Filename misspelled
- Permission issues

#### Example: Reading Missing File
```python
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()
```

**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

#### Solution: Handle the Exception
```python
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
```

**Result:** `Sorry, the file alice.txt does not exist.`

### 3.6 Analyzing Text

#### Counting Words in a Book
```python
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

#### How split() Works:
```python
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```
- Separates string at spaces
- Returns list of words
- May include punctuation with words

### 3.7 Working with Multiple Files

#### Creating Reusable Function
```python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)
```

#### Analyzing Multiple Books
```python
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

**Sample Output:**
```
The file alice.txt has about 29465 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

### 3.8 Failing Silently

#### When to Fail Silently
Sometimes you want the program to continue without reporting every error.

#### Using the pass Statement
```python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # Do nothing
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
```

#### Result: Silent Failure
```
The file alice.txt has about 29465 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

#### Uses of pass:
- Placeholder for future code
- Silent error handling
- Syntactic requirement for empty blocks

### 3.9 Deciding Which Errors to Report

#### Factors to Consider:
- **User expectations**: Do they know which files should exist?
- **User needs**: What information helps them?
- **Program purpose**: Is missing file critical or optional?
- **User experience**: Avoid overwhelming with unnecessary information

#### Best Practices:
- Report errors that users can act upon
- Provide clear, actionable error messages
- Consider logging errors for developers while showing simpler messages to users
- Test error handling thoroughly

### 3.10 Try It Yourself Exercises (Exceptions)

#### Exercise 10-6: Addition
Handle ValueError when users enter text instead of numbers.

**Solution:**
```python
try:
    first_num = input("First number: ")
    second_num = input("Second number: ")
    result = int(first_num) + int(second_num)
except ValueError:
    print("Please enter valid numbers only.")
else:
    print(f"The sum is: {result}")
```

#### Exercise 10-7: Addition Calculator
Wrap in loop to continue after errors.

**Solution:**
```python
print("Enter 'q' to quit.")
while True:
    try:
        first_num = input("\nFirst number: ")
        if first_num == 'q':
            break
        second_num = input("Second number: ")
        if second_num == 'q':
            break
        result = int(first_num) + int(second_num)
    except ValueError:
        print("Please enter valid numbers only.")
    else:
        print(f"The sum is: {result}")
```

#### Exercise 10-8: Cats and Dogs
Create files and handle FileNotFoundError.

**Solution:**
```python
# Create the files first
cats = ['Whiskers', 'Mittens', 'Shadow']
dogs = ['Buddy', 'Max', 'Luna']

with open('cats.txt', 'w') as f:
    for cat in cats:
        f.write(f"{cat}\n")

with open('dogs.txt', 'w') as f:
    for dog in dogs:
        f.write(f"{dog}\n")

# Read and display files
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    else:
        print(f"\nContents of {filename}:")
        print(contents.rstrip())
```

#### Exercise 10-9: Silent Cats and Dogs
Modify to fail silently.

**Solution:**
```python
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nContents of {filename}:")
        print(contents.rstrip())
```

#### Exercise 10-10: Common Words
Count occurrences of 'the' in Project Gutenberg texts.

**Solution:**
```python
def count_common_words(filename, word):
    """Count how many times a word appears in a text."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word.lower())
        print(f"'{word}' appears {word_count} times in {filename}.")

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_common_words(filename, 'the')
    count_common_words(filename, 'the ')  # With space
```

---

## Part 4: Storing Data

### 4.1 Introduction to JSON

#### What is JSON?
- **JavaScript Object Notation**
- Common format for data exchange
- Human-readable and language-independent
- Perfect for storing Python data structures

#### Why Use JSON?
- Save user preferences and data
- Share data between programs
- Persist information between program runs
- Compatible with many programming languages

### 4.2 Using json.dump() and json.load()

#### Writing Data with json.dump()
```python
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
```

**Result in numbers.json:**
```json
[2, 3, 5, 7, 11, 13]
```

#### Reading Data with json.load()
```python
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)  # [2, 3, 5, 7, 11, 13]
```

#### Key Points:
- `json.dump()` takes data and file object
- `json.load()` reads data from file object
- Data looks like Python but stored as JSON
- File extension `.json` is conventional

### 4.3 Saving and Reading User-Generated Data

#### Saving User's Name
```python
import json

username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
print(f"We'll remember you when you come back, {username}!")
```

#### Reading User's Name
```python
import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f"Welcome back, {username}!")
```

#### Combined Program
```python
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
```

### 4.4 Refactoring

#### Why Refactor?
- Make code cleaner and easier to understand
- Break complex functions into simpler ones
- Each function has a single, clear purpose
- Easier to maintain and extend

#### Original Combined Function
```python
def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
```

#### First Refactor: Separate Username Retrieval
```python
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

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
```

#### Final Refactor: Separate All Functions
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
```

#### Benefits of Final Version:
- **Single Responsibility**: Each function has one clear job
- **Reusability**: Functions can be used in other contexts
- **Testability**: Each function can be tested independently
- **Readability**: Code purpose is immediately clear
- **Maintainability**: Changes are localized to specific functions

### 4.5 Try It Yourself Exercises (JSON)

#### Exercise 10-11: Favorite Number
Store and retrieve user's favorite number.

**Part 1 - Store Number:**
```python
import json

number = input("What's your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
```

**Part 2 - Read Number:**
```python
import json

filename = 'favorite_number.json'
with open(filename) as f:
    number = json.load(f)
print(f"I know your favorite number! It's {number}.")
```

#### Exercise 10-12: Favorite Number Remembered
Combine into one program.

**Solution:**
```python
import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print(f"I'll remember that {number} is your favorite!")
else:
    print(f"I know your favorite number! It's {number}.")
```

#### Exercise 10-13: Verify User
Check if current user matches stored username.

**Solution:**
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
        correct = input(f"Are you {username}? (y/n) ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

---

## Chapter Summary

### Key Concepts Mastered:

#### File Operations:
- **Reading files**: entire file vs. line-by-line
- **File paths**: relative vs. absolute paths
- **Writing files**: write mode, append mode
- **File handling**: using `with` statements for proper file closure

#### Exception Handling:
- **try-except blocks**: graceful error handling
- **Common exceptions**: ZeroDivisionError, FileNotFoundError, ValueError
- **else blocks**: code that runs only on success
- **Silent failure**: using `pass` statement
- **Error reporting strategy**: when to show vs. hide errors

#### Data Persistence:
- **JSON format**: storing and loading Python data structures
- **User data**: saving preferences and information
- **Cross-session data**: maintaining state between program runs

#### Code Organization:
- **Refactoring**: breaking complex functions into simpler ones
- **Single responsibility**: each function has one clear purpose
- **Code maintainability**: making code easier to understand and modify

### Skills Developed:
1. **Robust Programming**: Handle errors gracefully instead of crashing
2. **Data Analysis**: Process large text files and extract information
3. **User Experience**: Provide friendly error messages and remember user data
4. **Code Quality**: Write clean, organized, and maintainable code
5. **File Management**: Work with various file formats and handle missing files

### Real-World Applications:
- Data analysis on large datasets
- User preference storage
- Log file processing
- Configuration management
- Error logging and monitoring
- Cross-platform data sharing

This comprehensive understanding of files and exceptions forms the foundation for building robust, user-friendly Python applications that can handle real-world scenarios and unexpected situations gracefully.
