from pathlib import Path

cats = Path('chapter_10/text_cats.txt')
dogs = Path('chapter_10/text_dogs.txt')

for pets in cats, dogs:
    try:
        print(pets.read_text(), end='\n\n')
    except FileNotFoundError:
        print(f"The file \"{pets}\" does not exist.", end='\n\n')