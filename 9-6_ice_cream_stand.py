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

    def lets_see_what_this_eatery_can_do(self):
        if self.cuisine_type == "Steakhouse":
            print("You win again gravity!")

class Ice_Cream_Stand(Restaurant):
    def __init__(self, stand_name, flavours):
        super().__init__(stand_name, "Ice Cream")
        self.flavours = flavours

    def display_flavours(self):
        print("Available ice cream flavours:")
        for flavour in self.flavours:
            print(f'\t-{flavour}')

print()

flavours = ["Chocolate", "Mint", "Vanilla", "Pecan", "Gravy"]
ice_cream_stand = Ice_Cream_Stand("Yorkshire Gelato", flavours)

ice_cream_stand.describe_restaurant()
print()
ice_cream_stand.display_flavours()
print()

# steakhouse = Restaurant("Fry's", "Steakhouse")
# steakhouse.describe_restaurant()
# steakhouse.lets_see_what_this_eatery_can_do()