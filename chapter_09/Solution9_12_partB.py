from Solution9_11_part import User

class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, merda=[]):
        self.privilegio = merda

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privilegio:
            for item in self.privilegio:
                print(f"- {item}")
        else:
            print("- This user has no privileges.")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privilegiazzo = Privileges()
