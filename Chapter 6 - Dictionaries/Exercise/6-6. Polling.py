favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'michael', 'phil', 'anna']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for responding.")
    else:
        print(f"{person.title()}, please take the poll about you favorite programming language.")