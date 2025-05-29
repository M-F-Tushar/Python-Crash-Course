user_names = ['mahir', 'faysal','tusher','admin','jaden']

for username in user_names:
    if username == 'admin':
        print(F"Hello {username}, would you like to see the status report?")
    else:
        print(f"hello {username}, thank you for logging in again.")