from pathlib import Path

name = input('What is your name?: ')
path = Path('guest.txt')
print('Check guest.txt')
path.write_text('Hello ' + name)