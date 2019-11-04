import json
import requests
from bs4 import BeautifulSoup


class AlbumsParser:
    def __init__(self, artist_name):
        self.artist = artist_name

    def to_json(self):
        with open(f"{self.artist}.json", 'w') as file:
            file.write(json.dumps(self.fetch_albums(), indent=2))

    def fetch_albums(self):
        albums = []

        page = self.get_albums_page()
        for link in self.fetch_albums_links(page):
            albums.append(
                self.fetch_album(self.get_album_page(link))
            )

        return albums

    def get_albums_page(self, page_number: int = 1):
        return requests.get(
            f"https://www.last.fm/music/{self.artist}/"
            f"+albums?order={page_number}"
        ).text

    def to_json_in_seconds(self):
        """This method creates a new json file but with songs duration in
        seconds (int)"""
        new_data = self.fetch_albums()
        for item in new_data:
            for song in item['songs']:
                new_value = song['duration'].split(':')
                song_length = (int(new_value[0]) * 60) + int(new_value[1])
                song['duration'] = song_length

        with open(f"{self.artist}_in_seconds.json", 'w') as file:
            file.write(json.dumps(new_data, indent=2))

    @staticmethod
    def get_album_page(link: str):
        return requests.get(link).text

    @staticmethod
    def fetch_albums_links(albums_page: str):
        # defining what parser to use by the second parameter html.parser
        soup = BeautifulSoup(albums_page, 'html.parser')
        section = soup.find('section', {'id': 'artist-albums-section'})
        for a in section.findAll('a', {'class': 'link-block-target'}):
            yield f"http://www.last.fm/{a['href']}"

    @staticmethod
    def fetch_album(album_page: str) -> dict:
        soup = BeautifulSoup(album_page, 'html.parser')
        album_name = soup.find('h1').text
        year = int(soup.findAll('dd',
                                {
                                    'class': 'catalogue-metadata-description'
                                })[1].text.split()[-1])
        artist = soup.find('span', {'itemprop': 'name'}).text
        songs = []
        for tr in soup.find_all('tr', {'class': 'chartlist-row'}):
            songs.append({
                'name': tr.find(
                    'td',
                    {'class': 'chartlist-name'}
                ).text.replace('\n', '').strip(),
                'artist': artist,
                'duration': tr.find(
                    'td',
                    {'class': 'chartlist-duration'}
                ).text.replace('\n', '').strip(),
                'year': year,
                'album': album_name
            })

        return {
            'name': album_name,
            'year': year,
            'genre': None,
            'artist': artist,
            'songs': songs
        }

    @staticmethod
    def from_json_to_json_in_seconds(json_file, new_file_name):
        """This method takes an existing json file with songs duration
        in 00:00 format and creates a new file in seconds (int) format"""
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                for song in item['songs']:
                    new_value = song['duration'].split(':')
                    song_length = (int(new_value[0]) * 60) + int(new_value[1])
                    song['duration'] = song_length

            with open(new_file_name, 'w') as file1:
                file1.write(json.dumps(data, indent=2))


parser = AlbumsParser('Tame Impala')
# parser.to_json()
# parser.from_seconds('Tame Impala.json', 'Tame Impala_in_seconds.json')
# parser.to_json_in_seconds()
