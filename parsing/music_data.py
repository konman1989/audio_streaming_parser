import requests
from bs4 import BeautifulSoup


def get_artist_page(artist_name: str):
    # get any artist by their name
    return requests.get(f"https://www.last.fm/music/{artist_name}").text


def parse_artist_info(artist_page: str) -> tuple:
    soup = BeautifulSoup(artist_page, 'html.parser')
    artist_name = soup.find('h1').text
    try:
        location = soup.findAll(
            'dd',
            {'class': 'catalogue-metadata-description'}
        )[1].text
    except IndexError:
        location = 'undefined'
    return artist_name, location


print(fetch_album(get_album_page('https://www.last.fm/music/Nirvana/Lithium')))
# print(parse_artist_info(get_artist_page('Nirvana')))
# for link in fetch_albums_links(get_albums_page('Nirvana', 1)):
#     print(link)

# print(get_album_page('https://www.last.fm/music/Nirvana/Lithium'))