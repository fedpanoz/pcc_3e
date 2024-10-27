from pathlib import Path
import json 

oggetto = Path('C:/Users/shegu/Documents/GitHub/pcc_3e/chapter_10/storing_data/numeri.json')
contenuto = oggetto.read_text()
numerazzi = json.loads(contenuto)
print(numerazzi)
print(type(numerazzi))
