rivers ={
    'nile': 'egypt',
    'amazon': 'brazil',
    'jomuna': 'bangladesh',
}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\nThe following rivers are mentioned:")
for river in rivers.keys():
    print(river.title())

print("\nThe following countries are mentioned:")
for country in rivers.values():
    print(country.title())