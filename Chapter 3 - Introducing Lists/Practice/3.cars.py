cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()

print(cars)

cars.sort(reverse=True)

print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

#Sorting a List Temporarily with the sorted() Function

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

'''
Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase. There are several ways to interpret capital letters when determining a sort
order, and specifying the exact order can be more complex than we want to deal with
at this time. However, most approaches to sorting will build directly on what you
learned in this section
'''

#To reverse the original order of a list, you can use the reverse() method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

number = len(cars)
print(f"Number of cars {number}")
