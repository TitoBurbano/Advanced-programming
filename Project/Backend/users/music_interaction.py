"""
This file contains the class for user-music interactions.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import List
from ..music import Song, Playlist  

class MusicInteraction:
    """This class provides various interactions with music content."""

    def __init__(self):
        self.playlists = [] 
        self.liked_songs = {}  

    def search(self, keyword: str, songs: List[Song]) -> List[Song]:
        """
        Searches for songs based on a keyword.

        Args:
            keyword (str): The search keyword used to find songs.
            songs (List[Song]): List of available songs.

        Returns:
            List[Song]: A list of songs matching the given keyword.
        """
        
        return [song for song in songs if keyword.lower() in song.title.lower() or keyword.lower() in song.author.lower()]

    def create_playlist(self, playlist_name: str) -> Playlist:
        """
        Creates a new playlist with a given name.

        Args:
            playlist_name (str): The name of the new playlist.

        Returns:
            Playlist: The created playlist.
        """
        new_playlist = Playlist(playlist_code=len(self.playlists), name=playlist_name)
        self.playlists.append(new_playlist)
        return new_playlist

    def receive_suggestions(self, liked_songs: List[Song]) -> List[Song]:
        """
        Receives song suggestions based on user preferences or history.

        Returns:
            List[Song]: A list of suggested songs.
        """
        
        suggested_songs = []
        for song in liked_songs:
            suggested_songs.extend([s for s in liked_songs if s.author == song.author or s.genre == song.genre])

        return list(set(suggested_songs))

    def give_like(self, song: Song) -> None:
        """
        This method is used to like songs, indicating user preference.

        Args:
            song (Song): The song to like.
        """
        if song not in self.liked_songs:
            self.liked_songs[song] = 1  
        else:
            self.liked_songs[song] += 1