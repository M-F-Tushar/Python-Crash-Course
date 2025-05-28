# Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'fish', 'cat', 'bird', 'cat']
print("Original list:", pets)

while 'cat' in pets:
    pets.remove('cat')

print("List after removing 'cat':", pets)