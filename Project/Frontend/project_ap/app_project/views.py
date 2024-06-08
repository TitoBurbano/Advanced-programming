import hashlib
import psycopg2 
from django.http import JsonResponse

def get_genre_songs(request, genre_name):
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
        cursor.execute("SELECT * FROM songs WHERE genre = %s", (genre_name,))
        songs = cursor.fetchall()
    except psycopg2.Error as e:
        print("Error fetching songs:", e)
    finally:
        cursor.close()
        connection.close()
    return JsonResponse(songs, safe=False)

def add_song_to_playlist(request, playlist_name, song_title):
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
        message = f"Canción '{song_title}' agregada a la playlist '{playlist_name}'"
    except psycopg2.Error as e:
        print("Error adding song to playlist:", e)
        message = "Error adding song to playlist"
    finally:
        cursor.close()
        connection.close()
    return JsonResponse({"message": message})

def remove_song_from_playlist(request, playlist_name, song_title):
    try:
        connection = psycopg2.connect(
            dbname="project_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM playlist_songs WHERE playlist_name = %s AND song_title = %s", (playlist_name, song_title))
        connection.commit()
        message = f"Canción '{song_title}' eliminada de la playlist '{playlist_name}'"
    except psycopg2.Error as e:
        print("Error removing song from playlist:", e)
        message = "Error removing song from playlist"
    finally:
        cursor.close()
        connection.close()
    return JsonResponse({"message": message})

def get_playlist_songs(request, playlist_name):
    try:
        connection = psycopg2.connect(
            dbname="project_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT song_title FROM playlist_songs WHERE playlist_name = %s", (playlist_name,))
        songs = [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print("Error fetching songs from playlist:", e)
        songs = []
    finally:
        cursor.close()
        connection.close()
    return JsonResponse({"songs": songs})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            connection.commit()
            message = "User registered successfully"
        except psycopg2.IntegrityError:
            connection.rollback()
            message = "Username already exists"
        except psycopg2.Error as e:
            print("Error registering user:", e)
            message = "Error registering user"
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"message": message})
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s",
                (username, hashed_password)
            )
            user = cursor.fetchone()
            if user:
                message = "Login successful"
            else:
                message = "Invalid username or password"
        except psycopg2.Error as e:
            print("Error logging in:", e)
            message = "Error logging in"
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"message": message})    
    

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
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
            songs = []
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"songs": songs})

def create_playlist(request):
    if request.method == 'POST':
        playlist_name = request.POST.get('playlist_name')
        try:
            connection = psycopg2.connect(
                dbname="project_db",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO playlists (username, playlist_name) VALUES (%s, %s)", (request.user.username, playlist_name))
            connection.commit()
            message = "Playlist created successfully"
        except psycopg2.Error as e:
            print("Error creating playlist:", e)
            message = "Error creating playlist"
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"message": message})

def add_song_to_a_playlist(request):
    if request.method == 'POST':
        playlist_name = request.POST.get('playlist_name')
        song_title = request.POST.get('song_title')
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
            message = f"Song '{song_title}' added to playlist '{playlist_name}' successfully"
        except psycopg2.Error as e:
            print("Error adding song to playlist:", e)
            message = "Error adding song to playlist"
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"message": message})

def upload_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        duration = request.POST.get('duration')
        album = request.POST.get('album')
        url = request.POST.get('url')
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
            message = "Song uploaded successfully"
        except psycopg2.Error as e:
            print("Error uploading song:", e)
            message = "Error uploading song"
        finally:
            cursor.close()
            connection.close()
        return JsonResponse({"message": message})
