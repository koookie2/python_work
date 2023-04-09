from pathlib import Path
import json

path = Path('chapter_10/data_numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)