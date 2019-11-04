import datetime


class WrongArtistError(Exception):
    pass


class Artist:

    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.songs = []
        self.albums = []

    def __repr__(self):
        return self.name

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def albums_number(self):
        return len(self.albums)


class Album:

    def __init__(
            self, name: str, year: int,
            artist: Artist, genre: str = None
    ):
        self.name = name
        self.year = year
        self.genre = genre
        self.artist = artist
        self.songs = []
        self.artist.albums.append(self)

    def __repr__(self):
        return self.name

    @property
    def songs_number(self):
        return len(self.songs)

    @property
    def duration(self):
        # return reduce(lambda x, y: x.duration + y.duration, self.songs)
        return datetime.timedelta(
            seconds=sum(song.duration.seconds for song in self.songs)
        )


class Song:

    def __init__(
            self, name: str, artist: Artist,
            year: int, duration: int, album=None,
            features: list = None
    ):

        self.name = name
        self.artist = artist
        self.features = features
        self.year = year
        self.duration = datetime.timedelta(seconds=duration)
        self.album = album
        try:
            if self.artist == self.album.artist:
                self.album.songs.append(self)
            else:
                raise WrongArtistError("Album and artist don't match")
        except AttributeError:
            print('This song is a single')
        self.artist.songs.append(self)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    artist1 = Artist('Steve', 'UK')
    artist2 = Artist('John', 'USA')

    steve_album1 = Album('s_album1', 2019, artist1)
    john_album1 = Album('j_album1', 2018, artist2)
    john_album2 = Album('j_album2', 2017, artist2)


    steve_song1 = Song('s_song1', artist1, 2019, 180, steve_album1)
    steve_song2 = Song('s_song2', artist1, 2019, 220)
    john_song1 = Song('j_song1', artist2, 2017, 150, john_album1)
    john_song2 = Song('j_song2', artist2, 2018, 300, john_album2)
    john_song3 = Song('j_song3', artist2, 2019, 180, john_album1)
    # # Exception:
    # steve_song3 = Song('s_song3', artist1, 2019, 210, john_album1)

