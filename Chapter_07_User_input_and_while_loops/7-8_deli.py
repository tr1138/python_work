sandwich_orders = ["'am", 'cheese', 'cucumber', 'pickle', 'beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print()

print('Sandwiches made today:')
for sandwich in finished_sandwiches:
    print(sandwich.title())