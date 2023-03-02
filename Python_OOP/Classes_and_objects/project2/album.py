class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        songs_names = [el.name for el in self.songs]
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name not in songs_names:
            self.songs.pop(songs_names.index(song_name))
            return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return "Album {name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        info = [f'Album {self.name}']

        for song in self.songs:
            info.append(f'== {song.get_info()}')

        return '\n'.join(info)


