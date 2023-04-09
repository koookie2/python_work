from pathlib import Path
import json

path = Path('chapter_10/data_favorite_number.json')

favorite_number = input("What is your favorite number? ")
path.write_text(json.dumps(favorite_number))