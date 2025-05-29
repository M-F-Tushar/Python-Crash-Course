# Using continue in a Loop
current_number = 0
while current_number < 19:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print("\n")
# Avoiding Infinite Loops

x = 1
while x <=5:
    print(x)
    x += 1 # if this statement was missing than loop would run infinitely