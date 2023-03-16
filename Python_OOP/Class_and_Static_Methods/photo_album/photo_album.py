class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for i in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        if photos_count % 4:
            pages += 1
        return cls(int(pages))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(self.photos[i])}"
        else:
            return "No more free slots"

    def display(self):
        result = []
        result.append('-' * 11)
        for i in range(self.pages):

            result.append(('[] ' * len(self.photos[i]))[:-1])
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum.from_photos_count(12)
