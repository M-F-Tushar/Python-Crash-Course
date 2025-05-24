# === Equality and Inequality with strings ===
animal = 'cat'

print("Is animal == 'cat'? I predict True.")
print(animal == 'cat') # True

print("\nIs animal == 'dog'? I predict False.")
print(animal == 'dog') # False

print("\nIs animal == 'Cat'? I predict False.")
print(animal == 'Cat') # False (case-sensitive)

# === Using the lower() method ===
name = 'Tusher'

print("\nIs name.lower() == 'tusher'? I predict False.")
print(name.lower() == 'tusher') # True

print("Is name.lower() == 'TUSHER'? I predict False.")
print(name.lower() == 'TUSHER') # False (case-sensitive)

# === Numerical Tests ===
age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)  # True

print("Is age != 30? I predict True.")
print(age != 30)  # True

print("Is age > 20? I predict True.")
print(age > 20)  # True

print("Is age < 20? I predict False.")
print(age < 20)  # False

print("Is age >= 25? I predict True.")
print(age >= 25)  # True

print("Is age <= 24? I predict False.")
print(age <= 24)  # False

# === Tests Using and/or ===
height = 170
weight = 65

print("\nIs height > 160 and weight < 70? I predict True.")
print(height > 160 and weight < 70)  # True

print("Is height < 160 or weight > 70? I predict False.")
print(height < 160 or weight > 70)  # False

# === Test for Item in List ===
colors = ['red', 'green', 'blue']

print("\nIs 'green' in colors? I predict True.")
print('green' in colors)  # True

print("Is 'yellow' in colors? I predict False.")
print('yellow' in colors)  # False

# === Test for Item Not in List ===
print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)  # True

print("Is 'red' not in colors? I predict False.")
print('red' not in colors)  # False