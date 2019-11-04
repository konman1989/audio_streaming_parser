import unittest
from classes import Artist, Album, Song


class TestAlbumClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.artist1 = Artist('Steve', 'UK')
        cls.album1 = Album('s_album1', 2019, cls.artist1)
        cls.song1 = Song('s_song', cls.artist1, 2018, 180, cls.album1)

    def test_property_songs_number(self):
        self.song2 = Song('s_song2', self.artist1, 2019, 150, self.album1)
        self.assertEqual(self.artist1.songs_number, 2)

    def test_duration_returns_total_songs_time(self):
        print(self.album1.duration)

        # почему работает только с перевеодом результата в формат стринг?
        self.assertEqual(str(self.album1.duration), '0:03:00')
