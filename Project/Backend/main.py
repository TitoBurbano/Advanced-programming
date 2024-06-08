from fastapi import FastAPI
from music import Genre, Playlist
from users import User, Authentication

app = FastAPI()

genre_instance = Genre(name="default")
playlist = Playlist(name="default")
authentication = Authentication(
    dbname="project_db",
    user="postgres",
    password="postgres"
)
user = User(username="default")

@app.get("/genre/{genre_name}/songs")
def get_genre_songs(genre_name: str):
    """
    Obtiene todas las canciones de un género específico.
    
    Args:
        genre_name (str): Nombre del género.

    Returns:
        list: Lista de canciones en el género.
    """
    genre_instance.name = genre_name
    return genre_instance.get_genre_songs()

@app.post("/playlist/{playlist_name}/add-song")
def add_song_to_playlist(playlist_name: str, song_title: str):
    """
    Agrega una canción a una playlist específica.
    
    Args:
        playlist_name (str): Nombre de la playlist.
        song_title (str): Título de la canción.

    Returns:
        str: Mensaje de éxito o error.
    """
    playlist.name = playlist_name
    return playlist.add_song(song_title)

@app.delete("/playlist/{playlist_name}/remove-song")
def remove_song_from_playlist(playlist_name: str, song_title: str):
    """
    Elimina una canción de una playlist específica.
    
    Args:
        playlist_name (str): Nombre de la playlist.
        song_title (str): Título de la canción.

    Returns:
        str: Mensaje de éxito o error.
    """
    playlist.name = playlist_name
    return playlist.remove_song(song_title)

@app.get("/playlist/{playlist_name}/songs")
def get_playlist_songs(playlist_name: str):
    """
    Obtiene todas las canciones de una playlist específica.
    
    Args:
        playlist_name (str): Nombre de la playlist.

    Returns:
        list: Lista de canciones en la playlist.
    """
    playlist.name = playlist_name
    return playlist.get_playlist_songs()

@app.post("/register")
def register(username: str, password: str):
    """
    Registra un nuevo usuario.
    
    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña.

    Returns:
        str: Mensaje de éxito o error.
    """
    return authentication.register(username, password)

@app.post("/login")
def login(username: str, password: str):
    """
    Inicia sesión con un usuario registrado.
    
    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña.

    Returns:
        str: Mensaje de éxito o error.
    """
    return authentication.login(username, password)

@app.get("/search")
def search(keyword: str):
    """
    Busca canciones por palabra clave.
    
    Args:
        keyword (str): Palabra clave de búsqueda.

    Returns:
        list: Lista de canciones que coinciden con la palabra clave.
    """
    return user.search(keyword)

@app.post("/create-playlist")
def create_playlist(playlist_name: str):
    """
    Crea una nueva playlist.
    
    Args:
        playlist_name (str): Nombre de la playlist.

    Returns:
        str: Mensaje de éxito o error.
    """
    user.username = "default"  # Debería asignarse después del login
    return user.create_playlist(playlist_name)

@app.post("/add-song-to-playlist")
def add_song_to_a_playlist(playlist_name: str, song_title: str):
    """
    Agrega una canción a una playlist específica.
    
    Args:
        playlist_name (str): Nombre de la playlist.
        song_title (str): Título de la canción.

    Returns:
        str: Mensaje de éxito o error.
    """
    user.username = "default"  # Debería asignarse después del login
    return user.add_song_to_playlist(playlist_name, song_title)

@app.post("/upload-song")
def upload_song(title: str, artist: str, genre: str, duration: str, album: str, url: str):
    """
    Sube una nueva canción.
    
    Args:
        title (str): Título de la canción.
        artist (str): Artista de la canción.
        genre (str): Género de la canción.
        duration (str): Duración de la canción.
        album (str): Álbum de la canción.
        url (str): URL de la canción.

    Returns:
        str: Mensaje de éxito o error.
    """
    return user.upload_song(title, artist, genre, duration, album, url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)