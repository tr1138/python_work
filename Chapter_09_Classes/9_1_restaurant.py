class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} eatery')


    def open_restaurant(self):
        print(f'{self.name} is open for business!')


restaurant = Restaurant('Sunshine', 'Turkish')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()