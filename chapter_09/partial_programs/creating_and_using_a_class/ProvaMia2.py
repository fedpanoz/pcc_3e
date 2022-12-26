class User:
    def __init__(self, first, last, username, infomail):
        self.first = first
        self.last = last
        self.username = username
        self.infomail = infomail

    def describe_user(self):
        mesaggio = f"il mio nome è {self.first}, il cognome è {self.last}, la mia user è: {self.username}" \
                   f" la mia mail è: {self.infomail}"
        print(mesaggio)

    def greet_user(self):
        messaggio2 = f"Thanks a lot {self.first} {self.last}"
        print(messaggio2)


alberto = User('Pino', 'fosforo', 'pipoolone', 'asdas@gmail.com')
LaGrandePina = User("Pina", "La Grande", "LGPina", "LaPina@gmail.com")
alberto.describe_user()
print(alberto.infomail)
alberto.greet_user()
LaGrandePina.describe_user()
LaGrandePina.greet_user()




