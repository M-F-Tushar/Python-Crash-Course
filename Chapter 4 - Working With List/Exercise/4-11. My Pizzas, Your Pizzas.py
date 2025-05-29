pizzas = ["Neapolitan Style Pizza", "Chicago Style Pizza", "New York Style Pizza"]
friend_pizzas = pizzas[:]

pizzas.append("Basi pizza")

friend_pizzas.append("Desi pizza")

print("My favorite pizzas are :")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are :")
for pizza in friend_pizzas:
    print(pizza)