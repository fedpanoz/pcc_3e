from pathlib import Path
import json

nome = input('dimmi il tuo nome:\n')
oggetto = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/storing_data/utenza.json')
contenuto = json.dumps(nome)
oggetto.write_text(contenuto)

print(f'ben tornato {nome}')
print(type(contenuto))