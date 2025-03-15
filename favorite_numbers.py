favorite_numbers = {'douglas': [42, 7, 98],
                    'jean': [359, 1701],
                    'kathryn': [7]
                    }

for person, nums in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for num in nums:
        print(num)
    print()