from pathlib import Path
import json

numeri = [1, 2, 3, 478, 99]
oggetto = Path('C:/Users/shegu/Documents/GitHub/pcc_3e/chapter_10/storing_data/numeri.json')
contenuto = json.dumps(numeri)
oggetto.write_text(contenuto)