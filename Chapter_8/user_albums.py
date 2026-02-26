def make_album(artist_name, album_title):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name, 'title': album_title}
    return album
while True:
    print("\nPlease tell me about an album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)