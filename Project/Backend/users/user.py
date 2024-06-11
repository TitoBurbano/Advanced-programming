"""
This file contains the class that represents a Musicat user.

Author: Tito Burbano Plazas <titolaejandro3118@gmail.com>
"""


import psycopg2

class User:
    """
    This class shows the different actions that a musicat user could perform.
    """
    def __init__(self, username):
        self.username = username

    def search(self, keyword):
        """
        This method is used to find a song that is registered by a keyword.

        Args:
        keyword (str): Search keyword.

        Returns:
        list: List of songs that match the keyword.
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
            cursor.execute("SELECT * FROM songs WHERE title ILIKE %s", ('%' + keyword + '%',))
            songs = cursor.fetchall()
        except psycopg2.Error as e:
            print("Error searching for songs:", e)
        finally:
            cursor.close()
            connection.close()
        return songs

    def create_playlist(self, playlist_name):
        """
        This method allows the user to create a new playlist.
        
        Args:
        playlist_name (str): Name of the playlist.

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
            cursor.execute("INSERT INTO playlists (username, playlist_name) VALUES (%s, %s)", (self.username, playlist_name))
            connection.commit()
        except psycopg2.Error as e:
            print("Error creating playlist:", e)
        finally:
            cursor.close()
            connection.close()

    def add_song_to_playlist(self, playlist_name, song_title):
        """
        This method allows the user to add a song to a playlist, but not from within the playlist.
        
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
            cursor.execute("INSERT INTO playlist_songs (playlist_name, song_title) VALUES (%s, %s)", (playlist_name, song_title))
            connection.commit()
        except psycopg2.Error as e:
            print("Error adding song to playlist:", e)
        finally:
            cursor.close()
            connection.close()

    def upload_song(self, title, artist, genre, duration, album, url):
        """
        This method allows the user to upload a song to the website.

        Args:
        title (str): Song title.
        artist (str): Artist of the song.
        genre (str): Genre of the song.
        duration (str): Duration of the song.
        album (str): Album of the song.
        url (str): URL of the song.

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
            cursor.execute("INSERT INTO songs (title, artist, genre, duration, album, url) VALUES (%s, %s, %s, %s, %s, %s)", (title, artist, genre, duration, album, url))
            connection.commit()
        except psycopg2.Error as e:
            print("Error uploading song:", e)
        finally:
            cursor.close()
            connection.close()
