from pathlib import Path


gino = Path('pi_digits.txt')
contents = gino.read_text()

lines = contents.splitlines()
for line in lines:
  print(line)
