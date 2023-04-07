from pathlib import Path

contents = "I love programming."
contents += "\nI love creating new games."
contents += "\nI also love working with data."

path = Path('chapter_10/programming.txt')
path.write_text(contents)