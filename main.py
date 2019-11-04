from classes import Artist, Album, Song


if __name__ == '__main__':
    artist1 = Artist('Steve', 'UK')
    artist2 = Artist('John', 'USA')

    steve_album1 = Album('s_album1', 2019, 'Indie rock', artist1)
    john_album1 = Album('j_album1', 2018, 'Alternative rock', artist2)
    john_album2 = Album('j_album2', 2017, 'Heavy metal', artist2)

    steve_song1 = Song('s_song1', artist1, [artist2], 2019, 180, steve_album1)
    steve_song2 = Song('s_song2', artist1, [artist2], 2019, 220)
    john_song1 = Song('j_song1', artist2, [artist1], 2017, 150, john_album1)
    john_song2 = Song('j_song2', artist2, [artist1], 2018, 300, john_album2)
    john_song3 = Song('j_song3', artist2, [artist1], 2019, 180, john_album1)
    # Exception:
    steve_song3 = Song('s_song3', artist1, [artist2], 2019, 210, john_album1)

    # print(artist1.albums)
    # print(artist2.albums)
    # print(steve_album1.songs)
    # print(john_album1.songs)
    # print(artist1.songs)
    # print(artist2.songs)
    # print(john_album1.duration)
