# Positional Arguments
def describe_pet(pet_name, pet_type):
    """Display information about a pet."""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")
describe_pet('gili', 'cat')

# Multiple Function Calls
# Order Matters in Positional Arguments

describe_pet('jonny', 'dog')

# Keyword Arguments

def describe_pet(pet_name, pet_type):
    """Display information about a pet."""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='gili', pet_type='cat')
 
 # Default Values
def describe_pet(pet_name, pet_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

describe_pet('gili')