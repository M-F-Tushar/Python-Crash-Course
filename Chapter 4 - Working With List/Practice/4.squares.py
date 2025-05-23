squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# To write this code more concisely
#squares = []
#   for value in range(1,11):
#    squares.append(value**2)
#print(squares)

#list comprehension
# squres = [value**2 for value in range(1,11)]
#print(square)