from pathlib import Path
contenuto = Path('pi_digits.txt')
risultato = contenuto.read_text()
print(risultato)