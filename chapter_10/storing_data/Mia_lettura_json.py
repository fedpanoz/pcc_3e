from pathlib import Path
import json

oggetto = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/storing_data/utenza.json')
contenuto = oggetto.read_text()
richiamo_stringa = json.loads(contenuto)
print(f'La stringa richiamata$ {richiamo_stringa}')