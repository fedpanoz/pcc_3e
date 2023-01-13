from random import choice

bucket = [11, 14, 6, 89, 109, 44, 76, 93, 33, 456, 'A ', 'U', 'L', 'G', 'k']



def biglietto_vincente(bucket):
    ticket_vincente = []
    while len(ticket_vincente) < 4:
        item = choice(bucket)
        if item not in ticket_vincente:
            ticket_vincente.append(item)
    return ticket_vincente

biglietto_vittorioso = biglietto_vincente(bucket)

def biglietto_prova(bucket):
    ticket_prova = []
    while len(ticket_prova) < 4:
        item = choice(bucket)
        if item not in ticket_prova:
            ticket_prova.append(item)
    return ticket_prova

def test_tickets(ticket_prova, biglietto_vitorioso):
    for element in ticket_prova:
        if element not in biglietto_vitorioso:
            return False
    return True



giocate = 0
vincita = False
max_giocate = 1_000

while not vincita:
    nuovo_biglietto = biglietto_prova(bucket)
    vincita = test_tickets(nuovo_biglietto, biglietto_vittorioso)
    giocate += 1
    if giocate >= max_giocate:
        break

if vincita:
    print(f"L'hia fatto in {giocate} giocate")
else:
    print(f"Hai provato {giocate} giocate ma non l'hai indovinato")


