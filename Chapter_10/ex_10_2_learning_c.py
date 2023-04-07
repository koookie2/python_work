from pathlib import Path

path = Path('chapter_10/learning_python.txt')
contents = path.read_text().replace('Python', 'C')
print(contents, end='\n\n')

lines = contents.splitlines()
for line in lines:
    print(line) 