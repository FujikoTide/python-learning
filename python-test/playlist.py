from dataclasses import dataclass
from random import choices
from typing import List, Union


@dataclass
class Song:
    title: str
    artist: str


@dataclass
class Playlist:
    songs: List[Song]

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __iter__(self):
        return iter(self.songs)

    def __contains__(self, item: Union[str, Song]) -> bool:
        if isinstance(item, Song):
            return item in self.songs
        if isinstance(item, str):
            return any(song.title == item for song in self.songs)
        return False


song1 = Song("song1", "artist1")
song2 = Song("song2", "artist2")
song3 = Song("song3", "artist3")

songs = choices([song1, song2, song3], k=100)

playlist = Playlist(songs)
print(playlist)
print(len(playlist))
print("song5" in playlist)


def loop_song(playlist):
    for song in playlist:
        print(song)


loop_song(playlist)
