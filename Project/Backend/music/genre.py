"""
This file contains the information related to the "Genre" class

Author: Tito Alejandro Burbano Plazas <titoalejandro3118@gmail.com>
"""
import psycopg2

class Genre:
    """
    The genre class is created as an abstract representation of the behavior of a musical genre.
    """
    def __init__(self, name):
        self.name = name

    def get_genre_songs(self):
        """
        This method is used to obtain the list of songs that are within a musical genre.
        
        Args:
        genre_name (str): Name of the genre.

        Returns:
        list: List of songs in the genre.
        """
        songs = []
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM songs WHERE genre = %s", (self.name,))
            songs = cursor.fetchall()
        except psycopg2.Error as e:
            print("Error fetching songs:", e)
        finally:
            cursor.close()
            connection.close()
        return songs