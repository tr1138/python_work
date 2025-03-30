from pathlib import Path
import json

path = Path('favourite_num.json')
contents = path.read_text()
favnum = json.loads(contents)

print(f'I know your favourite number, it\'s {favnum}!')
