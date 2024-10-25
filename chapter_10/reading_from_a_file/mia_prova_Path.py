from pathlib import Path
oggetto = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/reading_from_a_file/prova1.txt')
contenuto = oggetto.read_text()
print(contenuto)