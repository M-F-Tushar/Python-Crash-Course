# Complete Guide to Testing Python Code

## Table of Contents
1. [Introduction to Testing](#introduction-to-testing)
2. [Testing Functions](#testing-functions)
3. [Unit Tests and Test Cases](#unit-tests-and-test-cases)
4. [Working with Passing and Failing Tests](#working-with-passing-and-failing-tests)
5. [Testing Classes](#testing-classes)
6. [Assert Methods](#assert-methods)
7. [The setUp() Method](#the-setup-method)
8. [Exercises with Solutions](#exercises-with-solutions)
9. [Best Practices and Summary](#best-practices-and-summary)

---

## Introduction to Testing

### Why Test Your Code?
Testing is a critical practice in programming that:
- **Proves your code works** as intended for all expected input types
- **Builds confidence** that your code will work correctly for other users
- **Enables safe code changes** by ensuring new features don't break existing functionality
- **Catches problems early** before users encounter them
- **Makes debugging easier** by identifying exactly what broke and when

### Key Testing Concepts
- **Unit Test**: Verifies one specific aspect of a function's behavior
- **Test Case**: Collection of unit tests that prove a function behaves correctly across all expected situations
- **Full Coverage**: Testing all possible ways a function can be used
- **Critical Behaviors**: The most important functions that must work correctly

---

## Testing Functions

### Example Function to Test

Let's start with a simple function that formats names:

```python
# name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

### Manual Testing Program

Before automated testing, you might test manually:

```python
# names.py
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

**Sample Output:**
```
Enter 'q' at any time to quit.
Please give me a first name: janis
Please give me a last name: joplin
    Neatly formatted name: Janis Joplin.
Please give me a first name: bob
Please give me a last name: dylan
    Neatly formatted name: Bob Dylan.
```

### Problems with Manual Testing
- **Time-consuming**: Must manually enter test data each time
- **Error-prone**: Easy to forget edge cases
- **Not repeatable**: Hard to run the same tests consistently
- **Difficult to scale**: Becomes impractical for complex programs

---

## Unit Tests and Test Cases

### Understanding unittest Module

Python's `unittest` module provides tools for automated testing:
- **unittest.TestCase**: Base class for creating test cases
- **Assert methods**: Verify that results match expectations
- **Test discovery**: Automatically runs methods starting with `test_`
- **Test reporting**: Provides detailed output about test results

### Creating Your First Test Case

```python
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

### Breaking Down the Test Structure

1. **Import statements**: Import `unittest` and the function to test
2. **Test class**: Inherits from `unittest.TestCase`
3. **Class naming**: Use descriptive names ending with "TestCase"
4. **Test methods**: Start with `test_` for automatic discovery
5. **Assert methods**: Verify expected vs actual results
6. **Main block**: Runs tests when file is executed directly

---

## Working with Passing and Failing Tests

### A Passing Test

When you run the test above:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

**Understanding the Output:**
- **Dot (.)**: Indicates one test passed
- **Time**: Shows how long tests took to run
- **OK**: All tests in the test case passed

### Creating a Failing Test

Let's modify our function to require a middle name:

```python
# name_function.py (modified)
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

Running the same test now produces:

```
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_name_function.py", line 8, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'
----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

**Understanding Failure Output:**
- **E**: Indicates an error occurred
- **Error location**: Shows which test failed
- **Traceback**: Details about what went wrong
- **FAILED**: Summary of test results

### Responding to Failed Tests

**Golden Rule**: When a test fails, fix the code, not the test!

The test is telling us our change broke existing functionality. Let's fix it by making the middle name optional:

```python
# name_function.py (fixed)
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

Now the test passes again:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### Adding More Tests

Add a test for middle names:

```python
# test_name_function.py (expanded)
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

Running both tests:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

---

## Testing Classes

### Example Class to Test

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
```

### Using the Class

```python
# language_survey.py
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

### Testing the Class

```python
# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
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

---

## Assert Methods

### Common Assert Methods

| Method | Use Case | Example |
|--------|----------|---------|
| `assertEqual(a, b)` | Verify a equals b | `self.assertEqual(result, 'Expected')` |
| `assertNotEqual(a, b)` | Verify a does not equal b | `self.assertNotEqual(result, 'Wrong')` |
| `assertTrue(x)` | Verify x is True | `self.assertTrue(user.is_active)` |
| `assertFalse(x)` | Verify x is False | `self.assertFalse(user.is_banned)` |
| `assertIn(item, list)` | Verify item is in list | `self.assertIn('apple', fruits)` |
| `assertNotIn(item, list)` | Verify item is not in list | `self.assertNotIn('spam', emails)` |

### Detailed Examples

```python
import unittest

class ExampleTests(unittest.TestCase):
    
    def test_equality(self):
        """Test assertEqual and assertNotEqual"""
        result = 5 + 5
        self.assertEqual(result, 10)
        self.assertNotEqual(result, 9)
    
    def test_boolean_values(self):
        """Test assertTrue and assertFalse"""
        is_valid = True
        is_expired = False
        self.assertTrue(is_valid)
        self.assertFalse(is_expired)
    
    def test_membership(self):
        """Test assertIn and assertNotIn"""
        colors = ['red', 'green', 'blue']
        self.assertIn('red', colors)
        self.assertNotIn('yellow', colors)
```

---

## The setUp() Method

### Problem with Repetitive Test Setup

In our survey tests, we're creating the same objects repeatedly:

```python
# Repetitive code
def test_store_single_response(self):
    question = "What language did you first learn to speak?"  # Repeated
    my_survey = AnonymousSurvey(question)  # Repeated
    # ... rest of test

def test_store_three_responses(self):
    question = "What language did you first learn to speak?"  # Repeated
    my_survey = AnonymousSurvey(question)  # Repeated
    # ... rest of test
```

### Solution: Using setUp()

```python
# test_survey.py (improved)
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

### How setUp() Works

1. **Automatic execution**: Python runs `setUp()` before each test method
2. **Instance variables**: Objects created with `self.` are available in all test methods
3. **Fresh start**: Each test gets a clean copy of the setup objects
4. **Code reduction**: Eliminates repetitive setup code

---

## Exercises with Solutions

### Exercise 11-1: City, Country

**Task**: Write a function that accepts a city and country name, returning a formatted string. Test it thoroughly.

**Solution:**

```python
# city_functions.py
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

# test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_country function."""
    
    def test_city_country(self):
        """Test function with city and country."""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')
    
    def test_city_country_different_case(self):
        """Test function handles different cases."""
        result = city_country('NEW YORK', 'usa')
        self.assertEqual(result, 'New York, Usa')

if __name__ == '__main__':
    unittest.main()
```

### Exercise 11-2: Population

**Extended Task**: Modify function to include optional population parameter.

**Solution:**

```python
# city_functions.py (updated)
def city_country(city, country, population=None):
    """Return a formatted city, country string with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

# test_cities.py (updated)
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_country function."""
    
    def test_city_country(self):
        """Test function with city and country only."""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Test function with city, country, and population."""
        result = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')
    
    def test_city_country_large_population(self):
        """Test with a very large population number."""
        result = city_country('tokyo', 'japan', population=37400068)
        self.assertEqual(result, 'Tokyo, Japan - population 37400068')

if __name__ == '__main__':
    unittest.main()
```

### Exercise 11-3: Employee

**Task**: Create and test an Employee class with salary and raise functionality.

**Solution:**

```python
# employee.py
class Employee:
    """Represent an employee with salary management."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Store employee information."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=5000):
        """Give the employee a raise."""
        self.annual_salary += raise_amount

# test_employee.py
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for Employee class."""
    
    def setUp(self):
        """Create an employee for testing."""
        self.employee = Employee('John', 'Doe', 50000)
    
    def test_give_default_raise(self):
        """Test default raise of $5000."""
        original_salary = self.employee.annual_salary
        self.employee.give_raise()
        expected_salary = original_salary + 5000
        self.assertEqual(self.employee.annual_salary, expected_salary)
    
    def test_give_custom_raise(self):
        """Test custom raise amount."""
        original_salary = self.employee.annual_salary
        custom_raise = 7500
        self.employee.give_raise(custom_raise)
        expected_salary = original_salary + custom_raise
        self.assertEqual(self.employee.annual_salary, expected_salary)
    
    def test_employee_attributes(self):
        """Test that employee attributes are stored correctly."""
        self.assertEqual(self.employee.first_name, 'John')
        self.assertEqual(self.employee.last_name, 'Doe')
        self.assertEqual(self.employee.annual_salary, 50000)

if __name__ == '__main__':
    unittest.main()
```

---

## Best Practices and Summary

### Testing Best Practices

1. **Start Small**: Begin with simple tests for critical functions
2. **Test Edge Cases**: Include boundary conditions and unusual inputs
3. **Use Descriptive Names**: Test method names should clearly indicate what they test
4. **Keep Tests Independent**: Each test should work regardless of others
5. **Test Both Success and Failure**: Include tests for error conditions
6. **Update Tests with Code**: Modify tests when you change functionality

### When to Write Tests

**Always Test:**
- Functions that handle user input
- Functions that process data
- Classes that manage important state
- Code that interfaces with external systems

**Consider Testing:**
- Complex algorithms
- Functions with multiple branches
- Code that's been buggy in the past

### Understanding Test Output

**Test Result Characters:**
- `.` (dot): Test passed
- `E`: Error occurred during test
- `F`: Test assertion failed

**Reading Test Results:**
- Count dots to see how many tests passed
- Read error messages to understand failures
- Use traceback information to locate problems

### Testing Tools Beyond unittest

While this chapter focuses on `unittest`, Python offers other testing tools:
- **pytest**: More concise syntax and powerful features
- **doctest**: Tests embedded in docstrings
- **mock**: For testing code that depends on external services
- **coverage**: Measures how much of your code is tested

### Final Thoughts

Testing is an investment that pays off by:
- **Reducing debugging time**: Find problems early
- **Enabling confident refactoring**: Change code without fear
- **Documenting expected behavior**: Tests serve as examples
- **Building professional credibility**: Shows code quality awareness

Start incorporating tests into your projects gradually. Even a few tests for your most important functions can make a significant difference in code quality and maintainability.
