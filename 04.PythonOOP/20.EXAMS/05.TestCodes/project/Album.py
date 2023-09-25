from Song import Song


class Album:

    def __init__(self, name, song: Song):
        self.name = name
        self.published = False
        self.songs = [song]

    def add_song(self, song: Song):
        if song in self.songs:
            return f'Song is already in the album.'

        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song: Song):
        if self.published:
            return f"Cannot remove songs. Album is published."

        if song not in self.songs:
            return f"Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if not self.published:
            f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}'

        for song in self.songs:
            result += '\n'
            result += song.get_info()

        return result
