from pathlib import Path

contents = Path('chapter_10/text_pi_digits.txt').read_text()

for line in contents.splitlines():
    print(line)