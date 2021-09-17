from  spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from cleaner import SpotifyCleaner
import json


def load_config():
    with open("config.json") as f:
        config = json.load(f)
    return config

def get_token(username):
    config = load_config()
    scope = "playlist-modify-public playlist-read-private playlist-modify-private"
    client_id = config["client-id"]
    client_secret = config["client-secret"]
    redirect_url = config["redirect-url"]
    oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, show_dialog=True, scope=scope, redirect_uri=redirect_url)
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_url, oauth_manager=oauth)
    return token

print("Welcome to Spotify Cleaner")
username = input("Please enter your Spotify username: ")
token = get_token(username)
cleaner = SpotifyCleaner(token)
playlists = cleaner.get_playlists()
for i, playlist in enumerate(playlists):
    print(f"[{i+1}] {playlist.name}")
while True:
    choice = input("Select a playlist: ")
    if choice.isnumeric():
        choice = int(choice)
        choice -= 1
    else:
        continue
    if choice < 0 or choice >= len(playlists):
        continue
    else:
        playlist = playlists[choice]
        break

cleaner.get_songs(playlist)
clean = cleaner.clean_playlist(playlist)
print(clean.url)