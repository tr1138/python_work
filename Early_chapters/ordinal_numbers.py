nums = list(range(1,10))
print(nums)
print(range(1,10))
for num in nums:
    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f'{num}{suffix}')