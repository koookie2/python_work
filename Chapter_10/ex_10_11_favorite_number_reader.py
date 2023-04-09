from pathlib import Path
import json

path = Path('chapter_10/data_favorite_number.json')

favorite_number = json.loads(path.read_text())
print(f"I know your favorite number!\nIt’s {favorite_number}.")