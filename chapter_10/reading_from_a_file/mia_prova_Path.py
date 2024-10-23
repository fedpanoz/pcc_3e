from pathlib import Path
path = Path('pi_digits.txt')
risultato = path.read_text()
print(risultato)