class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [x for x in songs]
        published = False

    def add_song(self, song):
