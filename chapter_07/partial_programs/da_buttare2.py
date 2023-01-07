sandwich_orders = ['schifezza', 'pastrani', 'poldo', 'pastrani', 'nemo', 'pastrani', 'nasak', 'bruto']

for sandwich in sandwich_orders:
    if 'pastrani' in sandwich_orders:
        sandwich_orders.remove('pastrani')
print(sandwich_orders)