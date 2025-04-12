glossary = {
    'dictionary': 'A collection of key-value pairs. Each key is associated '
        + 'with a value. The key can be used to access the value.',
    'list': 'A collection of values that can be accessed by index. '
        + 'A list can be iterated through.',
    'python': 'An interpreted programming language.'
}

for word, definition in glossary.items():
    txt = f'{word.title()}:\n\t{definition}'
    print(txt + '\n')