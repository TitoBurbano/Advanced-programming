"""
This file contains the class to represent a song.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from datetime import datetime
from typing import Union

class Song:
    """This class represents the operation of a song."""

    def __init__(self, song_code: int, title: str, author: str, genre: str, length: int, album: Union[str, None], release_date: datetime, audio_url: str):

        self.song_code = song_code
        self.title = title
        self.author = author
        self.genre = genre
        self.length = length
        self.album = album
        self.release_date = release_date
        self.audio_url = audio_url

    def play(self) -> dict:
        """Returns information to play a song."""
        return {
            "action": "play",
            "audio_url": self.audio_url,
            "title": self.title,
            "author": self.author
        }

    def add_to_playlist(self, playlist) -> None:
        """
        This method adds the song to a playlist.

        Args:
           playlist: Playlist to which the song will be added.
        """
        if self in playlist.songs:
            print(f"'{self.title}' is already in '{playlist.name}'.")
        else:
            playlist.add_song(self)
            print(f"'{self.title}' added to '{playlist.name}'.")

    def is_new_launch(self) -> bool:
        """
        This method checks if the song is a new release.

        Returns:
           bool: True if the song is a new release, False otherwise.
        """
        current_date = datetime.now()

        return (current_date - self.release_date).days <= 15