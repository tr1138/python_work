def make_album(artist, title, num_of_songs=None):
    return {'artist': artist, 'title': title, 'number of songs': num_of_songs}

# print(make_album('Crush 40', 'Live and Learn'))
# print(make_album('Queen', 'Killer Queen'))
# print(make_album('Jackson', 'Thriller'))
# print(make_album('765', 'M@asterpiece', 18))

while True:
    print("Press 'q' to quit.")
    
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    num_of_songs = input("Number of songs: ")
    if num_of_songs == 'q':
        break
    
    print(make_album(artist, title, num_of_songs))