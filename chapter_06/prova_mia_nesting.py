alieni = []
for numero_alieni in range(10):
    nuovo_alieno = {'colore': 'verde', 'punti': 4, 'velocita': 'lenta'}
    alieni.append(nuovo_alieno)
for alieno in alieni:
    print(alieno)

print()

for alieno in alieni[:4]:
    if alieno['colore'] == 'verde':
       alieno['colore'] = 'giallo'
       alieno['punti'] = 877
       alieno['velocita'] = 'A Bombazza'

for alieno in alieni:
    print(alieno)
print()

print(alieni[4])