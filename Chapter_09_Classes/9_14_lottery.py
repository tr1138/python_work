from random import choice

digits = tuple([str(num) for num in range(10)] + 
             [chr(char) for char in range(ord('A'), ord('A') + 5)])

# print(digits)
# print(f'Digit count: {len(digits)}')
# for digit in digits:
#     print(digit)
# print()

winner = ""
for i in range(4):
    selection = choice(digits)
    # print(selection)
    winner += selection

print(f'The winning ticket is: {winner}')