import datetime
from functools import reduce


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

    def __init__(self, name: str, year: int, genre: str, artist: Artist):
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

    def __init__(self, name: str, artist: Artist, features: list,
                 year: int, duration: int, album=None):

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
                raise WrongArtistError
        except WrongArtistError:
            print("Album and artist don't match")
        except AttributeError:
            print('This song is a single')
        self.artist.songs.append(self)

    def __repr__(self):
        return self.name

