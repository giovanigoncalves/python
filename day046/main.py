import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

data = pd.read_csv("~/data_ggr_scripts/data.csv")

URL = data["URL"]
CLIENT_ID = data["CLIENT_ID"]
CLIENT_SECRET = data["CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = data["SPOTIPY_REDIRECT_URI"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "1992-09-07"
year = date.split('-')[0]
search_year = f"{1960}-{2022}"
response = requests.get(URL + date + "/")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

table_info = soup.find(name="div", class_="chart-results-list").find_all(name="div", class_="o-chart-results-list-row-container")
number = [row.find(name="span", class_="c-label").getText().strip() for row in table_info]
songs = [row.find(name="h3", class_="c-title").getText().strip().split(" (")[0] for row in table_info]
singers = [row.find(name="li", class_="lrv-u-width-100p").find(name="span", class_="c-label").getText().strip() for row in table_info]

songs_singers_list = [(songs[j], singers[j]) for j in range(len(songs))]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-private',
                                               show_dialog=True,
                                               cache_path="~/data_ggr_scripts/lesson_46.txt"
                                               )
                     )

uris = []
urls = []
error = 0
for (song, singer) in songs_singers_list:
    result = sp.search(q=f"track:{song} artist:{singer} year:{search_year}", type='track')
    try:
        uris.append(result["tracks"]["items"][0]["uri"])
        urls.append(result["tracks"]["items"][0]["external_urls"]["spotify"])
    except IndexError:
        print(f"'{song}' does not exist on Spotify. Skipped.")
        error += 1

uri_url = [(uris[i], urls[i]) for i in range(len(urls))]

user_id = sp.me()["id"]
playlist_name = date + " Billboard 100"
playlist = sp.user_playlist_create(user=user_id,
                                   name=playlist_name,
                                   public=False)

sp.playlist_add_items(playlist["id"], items=uris)
