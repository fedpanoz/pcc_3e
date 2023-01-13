from pathlib import Path
zizza = Path('pi_digits.txt')
da_scrivere = zizza.read_text()
print(da_scrivere.rstrip())
print('Cazzone')