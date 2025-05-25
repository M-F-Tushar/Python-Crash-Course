favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for person, language in favorite_languages.items():
    print(f"{person.title()} favorite language is {language.title()}")

# looping through all key-value pairs

for person in favorite_languages.keys():
    print(person.title())

# Looping through the keys is actually the default behavior when looping through a dictionary
for person in favorite_languages:
    print(person.title())


friends = ['phil', 'sarah']
for person in favorite_languages.keys():
    print(person.title())
    if person in friends:
        print(f"\t{person.title()}, I see you love {language}")


# find out if a particular person was polled.

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictonary's keys in a sorted order

for person in sorted(favorite_languages.keys()):
    print(f"{person.title()}, thank you for taking the poll.")

# looping through all values in a dictionary
print("The following language have been mentioned")
for language in favorite_languages.values():
    print(language.title())

# To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())