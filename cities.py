cities = {
        'london': { 'country': 'england',
                    'population': 7_000_000,
                    'fact': 'The River Thames flows through London.'},
        'paris': {  'country': 'france',
                    'population': 5_500_500,
                    'fact': 'Paris is in France!'},
        'glasgow': {'country': 'scotland',
                    'population': 4_000_000,
                    'fact': 'Birthplace of the Glasgow kiss.'}
                    }

for city, stats in cities.items():
    print(f"{city.title()} is a city in {stats['country'].title()} with a "
          f"population of {stats['population']:,}.\n\t{stats['fact']}\n")