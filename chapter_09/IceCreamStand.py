class Restaurant():


    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavs(self):
        for item in self.flavors:
            print(f"{item}\t\t", end='')

Gelateria = IceCreamStand('VillaBea',  'vegan')
Gelateria.display_flavs()