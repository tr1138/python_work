rivers = {
    'thames': 'england',
    'colorado': 'america',
    'amazon': 'brazil'
}

for river, country in rivers.items():
    print(f'\nThe {river.title()} runs through {country.title()}')

print('\n')

for river in rivers:
    print(river)

print('\n')
for country in rivers.values():
    print(country)