current_users = ['mahir', 'faysal', 'tusher', 'admin', 'jaden']

new_users = ['mahir', 'faysal', 'tusher', 'kamal', 'jade', 'john']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} will need to enter a new username.")
    else:
        print(f"{new_user} is available.")

print("\nAll usernames have been checked.")