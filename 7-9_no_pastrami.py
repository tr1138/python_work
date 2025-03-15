sandwich_orders = ["'am", 'cheese', 'pastrami', 'cucumber',  'pastrami', 
                   'pickle', 'beef', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print()

print('Sandwiches made today:')
for sandwich in finished_sandwiches:
    print(sandwich.title())