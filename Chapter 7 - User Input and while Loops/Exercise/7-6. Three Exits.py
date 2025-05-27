# 1. While condition directly checks for 'quit'
topping = ""

while topping != 'quit':
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping != 'quit':
        print(f"  --> Adding {topping} to your pizza.")

# 2. Use an active variable
active = True

while active:
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping == 'quit':
        active = False
    else:
        print(f"  --> Adding {topping} to your pizza.")

# 3. Use a break statement
while True:
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping == 'quit':
        break
    print(f"  --> Adding {topping} to your pizza.")
