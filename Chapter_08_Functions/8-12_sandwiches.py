def make_sandwich(*fillings):
    print("Sandwich fillings:")
    for filling in fillings:
        print(f"-{filling}")

make_sandwich('cheese', "pickle")
make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('cucumber')