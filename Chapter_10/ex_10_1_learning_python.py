from pathlib import Path

path = Path('chapter_10/text_learning_python.txt')
contents = path.read_text()
print(contents, end='\n\n')

lines = contents.splitlines()
for line in lines:
    print(line)