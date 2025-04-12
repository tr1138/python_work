print("Provide two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_num = input('\nFirst numnber: ')
    if first_num == 'q':
        break
    second_num = input('Second number: ')
    if second_num == 'q':
        break

    try:
        result = int(first_num) + int(second_num)
    except ValueError:
        print("Please enter only numbers or 'q' to quit.")
    else:
        print(f'{first_num} + {second_num} is {result}.')