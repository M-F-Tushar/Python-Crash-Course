users ={
    'aeinstein': {
        'first_name': 'albert',
        'last_name': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first_name': 'marie',
        'last_name': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name'].title()} {user_info['last_name'].title()}"
    location = user_info['location'].title()

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")