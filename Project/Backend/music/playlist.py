"""
This file contains the class to represent the playlists.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

import psycopg2

class Playlist:
    """
    The playlist class is created to show the behavior of a playlist.
    """
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song_title):
        """
        The add_song method is used to add a song directly from within the playlist.
        
        Args:
        playlist_name (str): Name of the playlist.
        song_title (str): Song title.

        Returns:
        str: Success or error message.
        """
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO playlist_songs (playlist_name, song_title) VALUES (%s, %s)", (self.name, song_title))
            connection.commit()
        except psycopg2.Error as e:
            print("Error adding song to playlist:", e)
        finally:
            cursor.close()
            connection.close()

    def remove_song(self, song_title):
        """
        The remove_song method is used to remove a song that is within a playlist.
        
        Args:
        playlist_name (str): Name of the playlist.
        song_title (str): Song title.

        Returns:
        str: Success or error message.
        """
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM playlist_songs WHERE playlist_name = %s AND song_title = %s", (self.name, song_title))
            connection.commit()
        except psycopg2.Error as e:
            print("Error removing song from playlist:", e)
        finally:
            cursor.close()
            connection.close()

    def get_playlist_songs(self):
        """
        This method is used to obtain a list of the songs that are within a playlist.
        
        Args:
        playlist_name (str): Name of the playlist.

        Returns:
        list: List of songs in the playlist.
        """
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT song_title FROM playlist_songs WHERE playlist_name = %s", (self.name,))
            self.songs = [row[0] for row in cursor.fetchall()]
        except psycopg2.Error as e:
            print("Error fetching songs from playlist:", e)
        finally:
            cursor.close()
            connection.close()
        return self.songs