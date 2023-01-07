sandwich_orders = ['schifezza', 'poldo', 'nemo', 'nasak', 'bruto']
immm_sand_orders = sandwich_orders[:]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
for sandwich in immm_sand_orders:
    to_pass = sandwich_orders.pop()
    finished_sandwiches.append(to_pass)

print("These sandwiches were made: ")
new_finished_sandwiches = finished_sandwiches.reverse()
for sandwich in finished_sandwiches:
    print(sandwich)

print(sandwich_orders)
print(finished_sandwiches)
print(immm_sand_orders)