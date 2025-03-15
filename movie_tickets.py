print()
age = ''
query = "Type 'quit' to exit.\nWhat is your age:\n"

# quit using conditional test
#
while age != 'quit':
    age = input(query)
    if age == 'quit':
        continue

# Loop controlled with active flag
#
# active = True
# while active:
#     age = input(query)
#     if age == 'quit':
#         active = False
#         continue

# quit using break
# 
# while True:    
#     age = input(query)
#     if age == 'quit':
#         break

    # common loop logic
    if not age.isnumeric():
        print("\nPlease enter your age.")
        continue # restart loop to ask for valid input
    elif int(age) < 3:
        price = 0
    elif int(age) <= 12:
        price = 10
    elif int(age) > 12:
        price = 15
    
    print(f"Your ticket is £{price}.\n")