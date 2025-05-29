print("Enter the pizza toppings you want (type 'quit' to finish):")

while True:
    topping = input("Topping: ")
    if topping.lower() == 'quit':
        print("Finished adding toppings.")
        break
    else:
        print(f"You have added: {topping}")
    