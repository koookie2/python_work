from pathlib import Path
import json

path = Path('chapter_10/data_username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")