from pathlib import Path
import json


def get_stored_userinfo(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None

def get_new_userinfo(path):
    """Prompt for a new username."""
    userinfo = {}
    userinfo['name'] = input("What is your name? ")
    userinfo['favnum'] = input("What is yourt favourite number? ")
    userinfo['favcolour'] = input("What is your favourite colour? ")
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def greet_user():
    """Greet the user by name."""
    path = Path('userinfo.json')
    userinfo = get_stored_userinfo(path)
    if userinfo:
        print(f"Welcome back, {userinfo['name']}!")
        print(f'Your favourite number is {userinfo['favnum']} and your '
              f'favourite colour is {userinfo['favcolour']}.')
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {userinfo['name']}!")

greet_user()