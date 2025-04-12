import users
import admins

privileges = ["can add post", "can delete post", "can ban-hammer"]
admin = admins.Admin("Joe", "Swanson", "Security", privileges)

admin.describe_user()
admin.privileges.show_privileges()
print()

user = users.User("Homer", "Sampson", "EHS")
user.describe_user()
print(f'User is admin: {user.admin}')