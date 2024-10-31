from pathlib import Path
import json

oggetto = Path('C:/Users/shegu/Documents/GitHub/pcc_3e/chapter_10/storing_data/utenza.json')
contenuto = oggetto.read_text()
risposta = json.loads(contenuto)

print(f'Ehi utente tu ti chiami {risposta}\n')