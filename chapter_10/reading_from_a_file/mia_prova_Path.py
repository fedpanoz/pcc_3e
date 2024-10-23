from pathlib import Path
path = Path('C:/Users/zizza/Documents/GitHub/pcc_3e/chapter_10/reading_from_a_file/prova1.txt')
contents = path.read_text()
print(contents)