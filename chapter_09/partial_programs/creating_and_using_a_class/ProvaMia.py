class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"My restaurant name is : '{self.restaurant_name}")
        print(f"The {self.restaurant_name} typic cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is finally open now")


my_restaurant = Restaurant("villa bea", "vegetariana")

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}\n\n")

guido_res = Restaurant('minchione', 'carnivora')
alberto_res = Restaurant('BellaF', 'indiana')
cinzia_res = Restaurant('La Gnocca', 'sexualfood')

guido_res.describe_restaurant()
alberto_res.describe_restaurant()
cinzia_res.describe_restaurant()


