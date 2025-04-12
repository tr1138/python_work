from pathlib import Path

def count_string_occurence_in_text_file(filename, string):
    """Prints the number of times the supplied string occurs in a utf-8
    formatted text file, ignoring case."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'File "{filename} not found."')
    else:
        count = contents.lower().count(string.lower())
        print(f'"{string.lower()}" occurs {count} times in {filename}')

files = ['the_time_machine.txt', 'war_of_the_worlds.txt']
strings = ['on', 'on ', 'one ', 'the', 'the ', 'there ']
for file in files:
    for string in strings:
        count_string_occurence_in_text_file(file, string)
    print()