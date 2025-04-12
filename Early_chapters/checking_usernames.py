current_users = ['alan', 'bob', 'Alice', 'admin', 'zebediah']
new_users = ['tom', 'thomas', 'toman', 'alice', 'zeBediah', 'geoff']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Username {new_user} is not available, please select another.')
    else:
        print(f'Username {new_user} is available.')

print(current_users)
print(current_users_lower)