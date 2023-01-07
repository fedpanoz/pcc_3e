places = {}

flag = True
while flag:
    nome = input("What's your name: ?")
    posto = input("What's the place you want to visit: ?")
    places[nome] = posto
    question = input("Do you want to take another poll: ?")
    if question == 'no':
        flag = False

print(places)
