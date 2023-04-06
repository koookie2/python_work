from pathlib import Path

path = Path('chapter 10\pi_digits.txt')
contents = path.read_text()
print(contents)