import users

class Admin(users.User):
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