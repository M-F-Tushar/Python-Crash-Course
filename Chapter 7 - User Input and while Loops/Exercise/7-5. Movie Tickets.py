while True:
    age = input("Enter your age (or type 'quit' to exit): ")

    if age == 'quit':
        print("Exiting the program.")
        break

    age = int(age)

    if age < 3:
        print("Your movie ticket is free!")
    elif age <= 12:
        print("Your movie ticket is $10.")
    else:
        print("Your movie ticket is $15.")