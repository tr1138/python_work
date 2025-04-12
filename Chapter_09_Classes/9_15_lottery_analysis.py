from random import choice

digits = tuple([str(num) for num in range(10)] + 
             [chr(char) for char in range(ord('A'), ord('A') + 5)])

# print(digits)
# print(f'Digit count: {len(digits)}')
# for digit in digits:
#     print(digit)
# print()

def select_ticket():
    ticket = ""
    for i in range(4):
        selection = choice(digits)
        # print(selection)
        ticket += selection
    return ticket


my_ticket = select_ticket()
print(f'Your ticket number is: {my_ticket}')

winner = ""
pull_count = 0

while my_ticket != winner:
    pull_count += 1
    winner = select_ticket()
    if pull_count % 5000 == 0 or pull_count == 1:
        print(f'Pull {pull_count}: {winner}')
    
print(f'The winning ticket is {winner}.\n'
      f'It took you {pull_count} pulls to win.')