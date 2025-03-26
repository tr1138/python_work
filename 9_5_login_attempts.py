class User:
    def __init__(self, first_name, last_name, department, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.admin = admin
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is assigned to the '
              f'{self.department} group.')
        if self.admin:
            print(f'{self.first_name} {self.last_name} is an administrator.')
    
    def greet_user(self):
        print(f'Welcome back {self.first_name} {self.last_name}.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('David', 'Robinson', 'Technical', True)

for i in range(106):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)