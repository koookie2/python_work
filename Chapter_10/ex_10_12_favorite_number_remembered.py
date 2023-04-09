from pathlib import Path
import json

path = Path('chapter_10/data_favorite_number.json')

if path.exists():
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number!\nIt’s {favorite_number}.")
else:
    favorite_number = input("What is your favorite number? ")
    path.write_text(json.dumps(favorite_number))