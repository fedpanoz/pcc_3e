from pathlib import Path
zizza = Path('pi_digits.txt')
contenuto = zizza.read_text()
righe = contenuto.splitlines()
print(righe)
print(type(righe))
print(righe[1])