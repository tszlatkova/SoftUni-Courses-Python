from typing import List
from .song import Song


class Album:

    def __init__(self, name: str, *songs: Song) -> None:
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        s = next((s for s in self.songs if s.name == song_name), None)
        if self.published:
            return "Cannot remove songs. Album is published."
        if s:
            self.songs.remove(s)
            return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_info = '\n'.join([f'== {s.get_info()}' for s in self.songs])
        return f"Album {self.name}\n{songs_info}"
