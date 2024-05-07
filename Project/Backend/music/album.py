"""
This file contains the class to represent music albums.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import List
from datetime import date
from .song import Song  

class Album:
    """This class represents a musical album."""

    def __init__(self, album_code: int, title: str, author: str, genre: str, release_date: date, list_songs: List[Song], is_new_launch: bool):
        self.album_code = album_code  
        self.title = title  
        self.author = author  
        self.genre = genre  
        self.release_date = release_date  
        self.list_songs = list_songs  
        self.is_new_launch = is_new_launch  

    def is_new_album(self) -> bool:
        """This method checks if the album is a new release to notify the user."""    
        current_date = date.today()
        return (current_date - self.release_date).days <= 15
    
    def get_songs(self) -> List[str]:
        """
        This method returns the list of song titles in the album.
        
        Returns:
            List[str]: A list of song titles in the album.
        """
        return [song.title for song in self.list_songs]

    def add_song(self, song: Song) -> None:
        """
        This method adds a song to the album.
        
        Args:
            song (Song): The song to add to the album.
        """
        if song not in self.list_songs:
            self.list_songs.append(song)
            print(f"'{song.title}' has been added to the album '{self.title}'.")
        else:
            print(f"'{song.title}' is already in the album '{self.title}'.")
