
class Song:
    def __init__(self, data):
        self.data = data

    def compare_song(self, cmp_song):
        if self.name == cmp_song.name:
            if self.artist_id == cmp_song.artist_id:
                if not cmp_song.is_explicit:
                    return True
        return False

    @property
    def name(self):
        if self.data.get("track"):
            return self.data["track"]["name"]
        else:
            return self.data["name"]

    @property
    def artist(self):
        if self.data.get("track"):
            return self.data["track"]["artists"][0]["name"]
        else:
            return self.data["artists"][0]["name"]

    @property
    def artist_id(self):
        if self.data.get("track"):
            return self.data["track"]["artists"][0]["id"]
        else:
            return self.data["artists"][0]["id"]

    @property
    def album(self):
        if self.data.get("track"):
            return self.data["track"]["album"]["name"]
        else:
            return self.data["album"]["name"]

    @property
    def id(self):
        if self.data.get("track"):
            return self.data["track"]["id"]
        else:
            return self.data["id"]

    @property
    def is_explicit(self):
        if self.data.get("track"):
            return self.data["track"]["explicit"]
        else:
            return self.data["explicit"]

    @property
    def is_local(self):
        if self.data.get("track"):
            return self.data["track"]["is_local"]
        else:
            return self.data["is_local"]