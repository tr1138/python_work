class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} eatery.')


    def open_restaurant(self):
        print(f'{self.name} is open for business!')

restaurants = []
restaurants.append(Restaurant('Sunshine', 'Turkish'))
restaurants.append(Restaurant('Dog and Duck', 'tranditional pub food'))
restaurants.append(Restaurant('Good Fortune', 'Chinese'))

for restaurant in restaurants:
    print()
    print(restaurant.name)
    print(restaurant.cuisine_type)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()