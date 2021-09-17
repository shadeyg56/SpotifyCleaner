import spotipy
from math import ceil
from playlist import Playlist
from song import Song
import os

def clear():
    if os.name in ('nt','dos'):
        os.system("cls")
    elif os.name in ('linux','osx','posix'):
        os.system("clear")
    else:
        print("\n") * 120


class SpotifyCleaner(spotipy.Spotify):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self.user_id = self.me()["id"]


    def get_playlists(self):
        result = self.current_user_playlists()
        playlists = []
        for playlist in result["items"]:
            playlist = Playlist(playlist)
            playlists.append(playlist)
        return playlists

    def get_clean_playlist(self, name):
        playlists = self.get_playlists()
        for playlist in playlists:
            if playlist.name == f"{name} (Clean)":
                return playlist
        return None

    def get_songs(self, playlist: Playlist):
        MAX_TRACKS = 100
        total_runs = ceil(playlist.track_count / MAX_TRACKS)
        tracks_gotten = 0
        for i in range(0, total_runs):
            result = self.playlist_tracks(playlist.id, offset=tracks_gotten)
            for song in result["items"]:
                playlist.songs.append(Song(song))
            tracks_gotten += MAX_TRACKS

    def clean_playlist(self, playlist: Playlist):
        MAX_TRACKS = 100
        self.user_playlist_create(self.user_id, f"{playlist.name} (Clean)", public=playlist.is_public)
        clean_playlist = self.get_clean_playlist(playlist.name)
        if clean_playlist:
            clean_songs = []
            i = 1
            total = 0
            for song in playlist.songs:
                clear()
                print("Cleaning playlist... Large playlists can take a while")
                print(f"Cleaning song {i} of {playlist.track_count}")
                if len(clean_songs) == MAX_TRACKS:
                    self.playlist_add_items(clean_playlist.id, clean_songs)
                    clean_songs = []
                if not song.is_local:
                    if song.is_explicit:
                        searches = self.search(f"{song.name} {song.artist}", type="track", limit=30)
                        for searched_track in searches["tracks"]["items"]:
                            searched_track = Song(searched_track)
                            is_same_song = song.compare_song(searched_track)
                            if is_same_song:
                                total += 1
                                clean_songs.append(searched_track.id)
                                break
                    else:
                        clean_songs.append(song.id)
                        total += 1
                i += 1
            if len(clean_songs) > 0:
                self.playlist_add_items(clean_playlist.id, clean_songs)
        print(f"Out of {playlist.track_count} songs, {total} were cleaned")
        return clean_playlist





        
