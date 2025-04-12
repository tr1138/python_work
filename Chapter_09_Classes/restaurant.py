class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} eatery.')


    def open_restaurant(self):
        print(f'{self.name} is open for business!')