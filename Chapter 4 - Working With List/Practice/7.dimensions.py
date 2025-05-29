# defining a tuple(values that can't change)

dimentions = (200, 50)
print(dimentions[0])
print(dimentions[1])
# tuples with one element 
my_t = (3,)
print(my_t[0])

# looping through all values in a tuple
dimentions = (200, 50)
for dimention in dimentions:
    print(dimention)


#Writing over a tuple

dimentions = (200, 50)
print("\nOriginal dimentions:")
for dimention in dimentions:
    print(dimention)

dimentions = (400, 100)
print("\nModified dimentions:")
for dimention in dimentions:
    print(dimention)