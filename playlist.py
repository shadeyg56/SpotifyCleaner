
class Playlist:
    def __init__(self, data):
        self.data = data
        self.songs = []
    
    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return self.data["id"]
    
    @property
    def track_count(self):
        return self.data["tracks"]["total"]

    @property
    def url(self):
        return self.data["external_urls"]["spotify"]

    @property
    def is_public(self):
        return self.data["public"]
    