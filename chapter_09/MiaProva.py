class User:
    def __init__(self, first_name, last_name, birth_day, residence, login_attempts):
        self.first_naem = first_name
        self.last_name = last_name
        self.birth_day = birth_day
        self.residence = residence
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"I am {self.first_naem} {self.last_name} born in {self.birth_day} and living in {self.residence}"
              f" and i've made {self.login_attempts} of login attempts")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

succa = User('Ciccio', 'Pasticcio', 10_03_1970, 'Loano', 5)

succa.describe_user()
succa.increment_login_attempts()
succa.increment_login_attempts()
succa.increment_login_attempts()
succa.describe_user()
succa.reset_login_attempts()
succa.describe_user()