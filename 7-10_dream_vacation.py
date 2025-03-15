poll_active = True
dream_destinations = {}

while poll_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would "
                     "you go?")
    dream_destinations[name] = response

    repeat = input("Would another person like to respond? y/n :")
    if repeat == 'n':
        poll_active = False

print()
for name in dream_destinations:
    print(f"{name} responded.")

print()
for name, response in dream_destinations.items():
    print(f"{name} would like to visit {response}.")