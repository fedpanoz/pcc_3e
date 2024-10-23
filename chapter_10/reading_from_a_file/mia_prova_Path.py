from pathlib import Path
path = Path('prova1.txt')
contents = path.read_text()
print(contents)