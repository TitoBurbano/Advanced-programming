"""
This file contains the class to represent music albums

Author: Tito Burbano Plazas <titoalejadnro3118@gmail.com>
"""

class Album:
    """This class represents a musical album"""

    def __init__(self, album_code: int, title: str, author: str, genre: str, release_date: date, list_songs: List[Song], is_new_launch: bool):
        pass

    def is_new_launch(self) -> bool:
        """This method is used to verify if the album is a new release and thus notify the user."""    
        pass