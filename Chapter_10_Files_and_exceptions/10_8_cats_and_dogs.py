from pathlib import Path

def print_text_file(filename):
    """Prints the contents of a text file"""
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f'Sorry, file "{filename}" not found.')
    else:
        print(contents)

files = ['Chapter_10_Files_and_exceptions/cats.txt', 
         'Chapter_10_Files_and_exceptions/dogs.txt']
for file in files:
    print_text_file(file)
    print()
