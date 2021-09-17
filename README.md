# SpotifyCleaner
A simple script to convert an explicit Spotify playlist into a non-explicit one

Takes a given Spotify playlist and checks every song and attempts to find a non-explicit version of it and add it to a clean version of the playlist. Songs that are already non-explicit are included. If a clean version of a song cannot be found then the song is not included. If the given playlist is private then the cleaned version will also be private, same goes for a public playlist.

## Prerequisites
* [A Spotify dev app](https://developer.spotify.com/dashboard/login)
* [Python](https://www.python.org/downloads/)

## Installation

```bash
pip install -r requirements.txt
```

After creating your Spotify app, open the config.json (rename config-example.json to config.json) and fill in your client id and secret. You probably don't need to change the redirect url but you **must** add the redirect url to your whitelisted urls on the Spotify dashboard or the login will not work.

## Running

```bash
python main.py
```