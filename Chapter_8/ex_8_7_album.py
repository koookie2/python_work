def make_album(artist, title, song_number=None):
    """Returns a dictionary of information about an album"""
    album = {'artist': artist, 'title': title}
    if song_number:
        album['song number'] = song_number
    return album

album = make_album('john lennon', 'imagine')
print(album)

album = make_album('beatles', 'white')
print(album)

album = make_album('elton john', 'the fox')
print(album)

album = make_album('imagine dragons', 'origins', 16)
print(album)