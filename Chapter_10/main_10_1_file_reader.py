from pathlib import Path

contents = Path('chapter_10/pi_digits.txt').read_text()

for line in contents.splitlines():
    print(line)