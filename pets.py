pets = []

pet = {'name': 'daifuku', 'animal': 'rabbit', 'owner': 'satoru'}
pets.append(pet)

pet = {'name': 'yuki', 'animal': 'cat', 'owner': 'mayu'}
pets.append(pet)

pet = {'name': 'komugi', 'animal': 'dog', 'owner': 'iroha'}
pets.append(pet)

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']} called "
          f"{pet['name'].title()}.")