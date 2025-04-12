users = ['alan', 'bob', 'alice', 'admin']
# users = []
if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Hello {user.title()}, would you like to see a status '
                  f'report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again')
else:
    print('We need to find some users!')