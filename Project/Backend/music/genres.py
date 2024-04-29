"""
This file contains the class that represents the musical genres.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

class Genre:
    """This class represents a musical genre."""

    def __init__(self, genre_code: int, name: str):
        self.genre_code = genre_code
        self.name = name

    def add_song(self, song: Song) -> None:
        """
        This method is used to add a song to the musical genre.
        
        Args: 
            song (Song): the song to add.
        """
        pass

    def get_info(self) -> List[Song]:
        """
        This method is used to get the list of songs of the album.
        
        Returns:
            List[Song]: The list of songs belonging to the genre.
        """
        pass