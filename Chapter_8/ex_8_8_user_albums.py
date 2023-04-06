def make_album(artist, title, song_number=None):
    """Returns a dictionary of information about an album"""
    album = {'artist': artist, 'title': title}
    if song_number:
        album['song number'] = song_number
    return album

while True:
    print("\nPlease tell me about an album", end= ' ')
    print("(enter 'q' at any time to quit):")
    
    artist = input("Album Artist: ")
    if artist == 'q':
        break
    
    title = input("Album Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(f"\nHello, {album}!")