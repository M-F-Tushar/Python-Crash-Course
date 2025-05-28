sandwich_orders = ['tuna sandwich', 'veggie sandwich', 'pastrami sandwich', 'ham sandwich', 'pastrami sandwich', 'pastrami sandwich']
finished_sandwich = []

print("The deli has run out of pastrami!\n")

while 'pastrami sanwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich.title()}")
    finished_sandwich.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwich:
    print(sandwich.title())