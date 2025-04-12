from pathlib import Path
import json

def get_stored_favnum(path):
    """Get's the favourite number stored in the supplied path if available."""
    if path.exists():
        contents = path.read_text()
        favnum = json.loads(contents)
        return favnum
    else:
        return None

def get_user_favnum(path):
    """Gets the user's favourite number and stores it in the supplied path."""
    favnum = input('What is your favourite number? ')
    content = json.dumps(favnum)
    path.write_text(content)

def show_favnum():
    """Shows the user's favourite number."""
    path = Path('favnum.json')
    favnum = get_stored_favnum(path)
    if favnum:
        print(f'I know your favourite number, it\'s {favnum}!')
    else:
        get_user_favnum(path)
        print("Thank's we'll remember next time!")

show_favnum()