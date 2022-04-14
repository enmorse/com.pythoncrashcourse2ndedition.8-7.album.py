def make_album(artists_name, album_title,
               no_of_songs=None):
    name = artists_name.title()
    title = album_title.title()

    album = {name, title, no_of_songs}
    return album


album_one = make_album("tool", "lateralus", 13)
album_two = make_album("sublime", "sublime", 17)
album_three = make_album("the beatles", "abbey road", 8)

print(album_one)
print(album_two)
print(album_three)
