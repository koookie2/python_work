from pathlib import Path
import json

numbers = [1, 3, 5, 7, 11 ,13]

path = Path('chapter_10/data_numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)