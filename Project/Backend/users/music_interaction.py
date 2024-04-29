"""
This file contains the class for music-related interactions.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

class MusicInteraction:
    """
    This class provides various interactions with music content, such as searching 
    for songs, creating playlists, receiving suggestions, and liking songs.
    """

    def __init__(self):
        pass
    
    def search(self, keyword: str) -> List[Song]:
        """
        This method is used to search for songs, based on a keyword

        Args:
            keyword (str): The search keyword used to find songs.

        Returns:
            List[Song]: A list of songs matching the given keyword.
        """
        pass
    
    def create_playlist(self, playlist_name: str) -> Playlist:
        """
        This method is used to creates a new playlist.

        Args:
            playlist_name (str): The name of the new playlist.

        Returns:
            Playlist: The created playlist.
        """
        pass
    
    def receive_suggestions(self) -> List[Song]:
        """
        Receives a list of song suggestions based on user preferences or history.

        Returns:
            List[Song]: A list of suggested songs.
        """
        pass
    
    def give_like(self, song: Song) -> None:
        """
        This method is used to Like songs, indicating user preference.

        Args:
            song (Song): The song to like.
        """
        pass