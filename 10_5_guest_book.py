from pathlib import Path

responses = ''
active = True

print("Please sign our guest book. Enter 'q' once done.")
while active:
    name = input('What is your name?: ')
    if name == 'q':
        break
    responses += name + '\n'

# print(responses)

path = Path('guest_book.txt')
path.write_text(responses)