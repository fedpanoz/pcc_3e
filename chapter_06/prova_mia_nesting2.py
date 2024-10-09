pizza = {'crust': 'thick',
         'toppings': ['acciughe', 'cipolla', 'speck', 'patatine']}

print(f"Hai ordinato una pizza con la crosta {pizza['crust']}")
print('Con i seguenti toppings:')
for topping in pizza['toppings']:
    print(topping)