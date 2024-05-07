"""
This file contains the class to represent the playlists.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import List, Union
from .song import Song

class Playlist:
    """This class represents the operation of a playlist."""

    def __init__(self, playlist_code: int, name: str):
        self.playlist_code = playlist_code
        self.name = name
        self.songs = []

    def add_song_to_playlist(self, song: Song) -> None:
        """
        This method is used to add a song to the playlist.

        Args:
            song (Song): The song that is going to be added.
        """
        if song not in self.songs:
            self.songs.append(song)
            print(f"'{song.title}' added to '{self.name}'.")
        else:
            print(f"'{song.title}' is already in '{self.name}'.")

    def delete_song(self, song: Song) -> None:
        """
        This method is used to delete a song from the playlist.

        Args:
            song (Song): The song that is going to be deleted.
        """
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song.title}' removed from '{self.name}'.")
        else:
            print(f"'{song.title}' is not in '{self.name}'.")

    def get_info(self) -> List[Song]:
        """
        This method is used to obtain playlist information, such as the list of songs.

        Returns:
            List[Song]: List of songs that are in the playlist.
        """
        return self.songs
    