"""
This file contains the class for user-music interactions.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models import Song, Playlist
from ..database import Base

class MusicInteraction:
    """
    This class provides various interactions with music content.
    """

    def __init__(self, db_url: str):
        """
        Initializes the MusicInteraction class with the database URL.

        Args:
            db_url (str): The URL for connecting to the PostgreSQL database.
        """
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def search(self, keyword: str) -> List[Song]:
        """
        Searches for songs based on a keyword.

        Args:
            keyword (str): The search keyword used to find songs.

        Returns:
            List[Song]: A list of songs matching the given keyword.
        """
        return self.session.query(Song).filter(
            (Song.title.ilike(f'%{keyword}%')) | 
            (Song.artist.ilike(f'%{keyword}%'))
        ).all()

    def create_playlist(self, playlist_name: str) -> Playlist:
        """
        Creates a new playlist with a given name.

        Args:
            playlist_name (str): The name of the new playlist.

        Returns:
            Playlist: The created playlist.
        """
        new_playlist = Playlist(name=playlist_name)
        self.session.add(new_playlist)
        self.session.commit()
        return new_playlist

    def receive_suggestions(self, liked_songs: List[Song]) -> List[Song]:
        """
        Receives song suggestions based on user preferences or history.

        Returns:
            List[Song]: A list of suggested songs.
        """
        suggested_songs = []
        for song in liked_songs:
            suggested_songs.extend(self.session.query(Song).filter(
                (Song.artist == song.artist) | (Song.genre == song.genre)
            ).all())

        return list(set(suggested_songs))

    def give_like(self, song_id: int) -> None:
        """
        This method is used to like songs, indicating user preference.

        Args:
            song_id (int): The ID of the song to like.
        """
        song = self.session.query(Song).get(song_id)
        if song:
            song.likes += 1
            self.session.commit()
