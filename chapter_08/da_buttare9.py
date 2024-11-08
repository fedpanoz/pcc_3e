def prova_dizionario(nome, cognome, età=None):
    '''Restituisce un dizionario con nome e cognome, con l'aggiunta dell'età.'''
    persona = {'nome': nome, 'cognome': cognome}
    if età:
        persona['età'] = età
    return persona

scenziato = prova_dizionario('Alberto', 'Einstein', età=76)
print(scenziato)
print(type(scenziato))

senza_età = prova_dizionario('Alberto', 'Einstein')
print(senza_età)
