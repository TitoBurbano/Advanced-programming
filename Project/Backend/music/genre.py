import psycopg2
class Genre:
    def __init__(self, name):
        self.name = name

    def get_genre_songs(self):
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