def my_car(fabbrica, modello, **supercar):
    supercar['produttore'] = fabbrica
    supercar['tipo'] = modello
    return supercar


bellaVettura = my_car('Wolkswagen', 'Golf', colore='arancione', cavalli=195)

print(bellaVettura)