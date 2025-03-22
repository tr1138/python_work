class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} eatery.')

    def open_restaurant(self):
        print(f'{self.name} is open for business!')
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, num):
        self.number_served += num
    


restaurant = Restaurant('Sunshine', 'Turkish')

print(restaurant.number_served)
restaurant.set_number_served(8)
print(restaurant.number_served)
restaurant.increment_number_served(25)
print(restaurant.number_served)