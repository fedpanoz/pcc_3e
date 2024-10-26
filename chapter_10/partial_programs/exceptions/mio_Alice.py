from pathlib import Path
oggetto = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/partial_programs/exceptions/alice.txt')
contenuto = oggetto.read_text(encoding='utf-8')
parole = contenuto.split()
print(type(parole))
print(len(parole))
print(parole[:33])
print(f'Il testo Alice e fatto di {len(parole)} parole')