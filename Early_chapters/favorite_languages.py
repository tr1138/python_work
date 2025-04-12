favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

pollees = ['sarah', 'ralph', 'apu', 'edward']

for pollee in pollees:
    if pollee in favorite_languages:
        txt = f'Thank you {pollee.title()} for completing the poll. Your '
        txt += f'favourite language is {favorite_languages[pollee].title()}.'
        print(txt)   
    else:
        txt = f'{pollee.title()}, you are welcome to complete our poll.'
        print(txt)