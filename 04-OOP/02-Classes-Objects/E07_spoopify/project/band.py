from typing import List
from .album import Album


class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: List[Album] = list()

    def add_album(self, album: Album) -> str:
        a: Album = next((a for a in self.albums if a.name == album), None)
        if a:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        a: Album = next((a for a in self.albums if a.name == album_name), None)
        if a:
            if a.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(a)
            return f"Album {a.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self) -> str:
        albums_info = '\n'.join([album.details() for album in self.albums])
        return f'Band {self.name}\n{albums_info}'
