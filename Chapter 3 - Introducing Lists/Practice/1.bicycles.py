bicycles = ['trek','conondale','redline','specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[3])

print(bicycles[-1])# Special syntax for accessing the last element of the list. This syntax is quite useful,
# because you’ll often want to access the last items in a list without knowing exactly how long the list is

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
