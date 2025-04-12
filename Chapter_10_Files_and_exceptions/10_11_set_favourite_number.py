from pathlib import Path
import json

favnum = input('What is your favourite number? ')
path = Path('favourite_num.json')
content = json.dumps(favnum)
path.write_text(content)