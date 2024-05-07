"""
This file contains the class that represents the musical genres.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import List
from .song import Song  
class Genre:
    """This class represents a musical genre."""

    def __init__(self, genre_code: int, name: str):
        self.genre_code = genre_code 
        self.name = name 
        self.songs = [] 

    def add_song(self, song: Song) -> None:
        """
        This method adds a song to the musical genre if it matches the genre name.
        
        Args: 
            song (Song): The song to add.
        """
        if song.genre == self.name:
            if song not in self.songs:
                self.songs.append(song)
                print(f"'{song.title}' has been added to '{self.name}'.")
            else:
                print(f"'{song.title}' is already in '{self.name}'.")
        else:
            print(f"'{song.title}' does not belong to '{self.name}'.")

    @staticmethod
    def find_or_create_genre(genre_name: str, genres: List[Genre], song: Song) -> Genre:
        """
        Finds an existing genre by name, or creates a new one if it doesn't exist, and adds the song.

        Args:
            genre_name (str): The name of the genre to find or create.
            genres (List[Genre]): The list of existing genres.
            song (Song): The song to be added to the genre.

        Returns:
            Genre: The found or newly created genre.
        """
        
        genre = next((g for g in genres if g.name == genre_name), None)

        if genre is None:
            genre = Genre(genre_code=0, name=genre_name)  
            genres.append(genre)

        genre.add_song(song)  
        return genre

    def get_info(self) -> List[str]:
        """
        This method returns a list of song titles in the genre.
        
        Returns:
            List[str]: The list of song titles belonging to the genre.
        """
        return [song.title for song in self.songs]  
