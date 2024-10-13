class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Pasticcio', 13)
print(type(my_dog))
print('gino')

print(f"il nome delmio cane è: {my_dog.name}")
print(f"L'età del mio cane è: {my_dog.age}")
print()
my_dog.roll_over()
print()
my_dog.sit()