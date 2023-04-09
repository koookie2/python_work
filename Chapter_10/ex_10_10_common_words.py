from pathlib import Path

book = Path('chapter_10/text_tom_sawyer.txt').read_text(encoding='utf-8')
print(f"The phrase \"the \" appears {book.lower().count('the ')} times in the book \"The Adventures of Tom Sawyer\".")