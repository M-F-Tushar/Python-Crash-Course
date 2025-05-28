sandwich_orders = ['tuna sandwich', 'veggie sandwich', 'pastrami sandwich', 'ham sandwich']

finished_sandwich= []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI made your {current_sandwich.title()}")
    finished_sandwich.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwich:
    print(sandwich.title())
    

