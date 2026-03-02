def make_album(artist_name, album_title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name, 'title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album
album = make_album('pink floyd', 'the dark side of the moon', tracks=10)
album = make_album('the beatles', 'abbey road')
print(album)