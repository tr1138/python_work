topping = ''
while topping != 'quit':
    topping = input("Please select a topping, enter 'quit' to exit. ")
    if topping != 'quit':
        print(f"{topping.title()} has been added to your pizza.")