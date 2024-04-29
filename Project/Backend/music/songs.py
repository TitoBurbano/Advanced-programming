"""
 This file contains the class to represent a song.
 
 Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
 """

class Song:
    """This class represents the operation of a song."""

    def __init__(self, song_code: int, title: str, author: str, genre: str, length: int, album: Union[str, None], is_new_launch: bool):
        self.song_code = song_code
        self.title = title
        self.author = author
        self.genre = genre
        self.length = length
        self.album = album
        self.is_new_launch = is_new_launch

    def play(self) -> None:
        """This method is used to play a song."""
        pass

    def add_to_playlist(self, playlist: "Playlist") -> None:
        """
        This method is used to add a song to a playlist.

        Args:
           playlist (Playlist): Playlist to which the song will be added.
        """
        pass

    def is_new_launch(self) -> bool:
        """
        This method is used to check if the song is a new release.

        Returns:
           bool: True if the song is a new release, False otherwise.
        """
        pass