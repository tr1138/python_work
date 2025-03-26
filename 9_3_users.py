class User:
    def __init__(self, first_name, last_name, department, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.admin = admin
    
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is assigned to the '
              f'{self.department} group.')
        if self.admin:
            print(f'{self.first_name} {self.last_name} is an administrator.')
    
    def greet_user(self):
        print(f'Welcome back {self.first_name} {self.last_name}.')

users = []
users.append(User('David', 'Robinson', 'Technical', True))
users.append(User('Steven', 'James', 'Engineering'))
users.append(User('Tim', 'Partridge', 'Technical'))

for user in users:
    print()
    user.describe_user()
    user.greet_user()