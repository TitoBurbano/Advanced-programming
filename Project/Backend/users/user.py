"""
This file contains the class that represents a user.

Author: Tito Burbano Plazas <titolaejandro3118@gmail.com>
"""


import psycopg2

class User:
    def __init__(self, username):
        self.username = username

    def search(self, keyword):
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
