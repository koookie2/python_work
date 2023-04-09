from pathlib import Path

path = Path('chapter_10/text_guest.txt')
names, name = '', input("What is your name? ")

while name != 'quit':
    names += f"{name}\n"
    name = input("What is your name? ")

path.write_text(names.rstrip())