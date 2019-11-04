import unittest
from classes import Artist, Album, Song, WrongArtistError


class TestSongCLass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.artist1 = Artist('Steve', 'UK')
        cls.artist2 = Artist('John', 'USA')
        cls.album1 = Album('s_album1', 2019, cls.artist1)
        cls.album2 = Album('j_album1', 2017, cls.artist2)
        cls.song1 = Song('s_song', cls.artist1, 2018, 180, cls.album1)
        cls.song2 = Song('j_song', cls.artist2, 2017, 150, cls.album2)

    def test_album_raises_error_if_artist_and_album_mismatch(self):
        with self.assertRaises(WrongArtistError):
            self.song3 = Song('s_song2', self.artist1, 2017, 140, self.album2)

