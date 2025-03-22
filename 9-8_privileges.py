class User:
    def __init__(self, first_name, last_name, department):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.admin = False
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

class Admin(User):
    def __init__(self, first_name, last_name, department, privileges):
        super().__init__(first_name, last_name, department)
        self.admin = True
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('User has the following privileges:')
        for privilege in self.privileges:
            print(f'\t-{privilege}')


privileges = ["can add post", "can delete post", "can ban-hammer"]
admin = Admin("Joe", "Swanson", "Security", privileges)

admin.describe_user()
print()
admin.privileges.show_privileges()
print()

user = User("Homer", "Sampson", "EHS")
user.describe_user()
print(f'User is admin: {user.admin}')