responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and vocation
    name = input("\n What is your name?")
    response = input("\nIf you could visit one place in the world, where would you go?")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another person respond? (yes/no)")
    if repeat.lower() == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")