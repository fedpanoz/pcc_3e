from pathlib import Path
import json

oggetto = Path('C:/Users/shegu/Documents/GitHub/pcc_3e/chapter_10/storing_data/utenza.json')
utente = input('Dimmi il tuo nome')
contenuto = json.dumps(utente)
oggetto.write_text(contenuto)
