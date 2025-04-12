people = []

person = {
    'first_name': 'Bob', 
    'last_name': 'Johnson', 
    'city': 'Duxford'
    }
people.append(person)

person = {
    'first_name': 'Maria', 
    'last_name': 'Swanson', 
    'city': 'Piza'
    }
people.append(person)

person = {
    'first_name': 'Raj', 
    'last_name': 'Smith', 
    'city': 'Colchester'
    }
people.append(person)

for person in people:
    print(f"{person['first_name']}'s last name is {person['last_name']}. "
        f"They live in {person['city']}.")