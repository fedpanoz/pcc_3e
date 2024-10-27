from pathlib import Path

def count_words(sentiero):
    oggetto = Path(sentiero)
    contenuto = oggetto.read_text(encoding='utf-8')
    parole = contenuto.split()
    numero_par = len(parole)
    print(f'\nI libro che ha titolo {oggetto} ha {numero_par} parole')
    
    
la_prova = input('dimmi il testo da contare')

count_words(la_prova)