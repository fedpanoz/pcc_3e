from pathlib import Path
oggetto = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/partial_programs/writing_to_a_file/scrivo.txt')
testo = 'Mi piace la programmazione\n'
testo += 'Pero mi piace anche il kitesurf\n'
testo += 'E anche le belle ragazze'
contenuto = oggetto.write_text(testo)