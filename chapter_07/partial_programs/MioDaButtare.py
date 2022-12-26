belli = ['Gino', 'Pazzo', 'Luca', 'Emanuela']
brutti = []
while belli:
    trasferendo = belli.pop()
    print(f"Esaminando {trasferendo}")
    brutti.append(trasferendo)
print(brutti)
print(f"\n{belli}")
print(type(brutti))