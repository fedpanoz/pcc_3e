class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")


class Privileges:
    def __init__(self, cazzate=[]):
        self.cazzate = ['Remove object', 'Making ice_creams', 'Eating sandwiches']

    def show_privileges(self):
        print(f"An admin can {self.cazzate[0]}, {self.cazzate[1]}, {self.cazzate[2]}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.cazzate = Privileges()







Ninuzzo = Admin('Nino', 'Fossforo', 'Fosfy', 'giggoò@gmail.com', 'Bardino')

Ninuzzo.cazzate.show_privileges()