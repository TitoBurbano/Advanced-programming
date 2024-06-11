"""
This file contains the class to represent a song.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""
class Song:
    """
    This class is an abstract representation of a song, it contains the attributes that make up a song.
    """

    def __init__(self, title, artist, genre, duration, album, url):
        
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.album = album
        self.url = url


   

    

   