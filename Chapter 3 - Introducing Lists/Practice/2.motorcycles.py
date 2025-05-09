motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)

motorcycle[0] = 'ducari'
print(motorcycle)

motorcycle.append('honda')
print(motorcycle    )

motorcycle = []

motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')

print(motorcycle)

motorcycle.insert(0, 'ducatu')# the insert() method opens a space at position 0 and stores the value 'ducati' at the location
print(motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # removing an item using the del statement
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()#Removing an Item Using the pop() Method
print(motorcycles)
print(popped_motorcycle)#The method removes the last item in a list, but it lets you work pop() with that item after removing it.

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")# Popping Items from any Position in a List

# When you want to delete a item in the list and not use them in any way, use the del statement, if you want to use an item as you remove it, use the pop() method

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')# If you only know the value of the item you want to remove, you can use the remove() method.
print(motorcycles)


#Let’s remove the value 'ducati' and print a reason for removing it from the list

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

