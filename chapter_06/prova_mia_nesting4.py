pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'anchoives', 'melone', 'anguria']
}

print(f"You ordered a pizza with {pizza['crust']} crosta e con i seguenti toppings:")
for topping in pizza['toppings']:
    print(f"{topping}")