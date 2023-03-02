class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums_names = [el.name for el in self.albums]
        if album_name in albums_names:
            if not self.albums[albums_names.index(album_name)].published:
                self.albums.pop(albums_names.index(album_name))
                return f"Album {album_name} has been removed."
            else:
                return "Album has been published. It cannot be removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        info = [f'Band {self.name}\n']
        for album in self.albums:
            info.append(album.details())

        return ''.join(info)
